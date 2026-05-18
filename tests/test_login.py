import allure

from data.user_factory import UserFactory
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.epic("Сайт Skyrexio")
@allure.feature("Страница логина")
class TestLoginPage:

    @allure.title("Логин существующего пользователя с корректными данными")
    @allure.description(
        "Тест проверяет, что при вводе корректных электронной почты и пароля "
        "зарегистрированного на сайте пользователя и последующем нажатии на кнопку входа "
        "происходит вход на сайт и открывается домашняя страница пользователя"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_pass_when_correct_existing_user(self, driver):
        user = UserFactory.correct_existing_user()

        open_login_page_from_main(driver)
        login_as(driver, user)

        home_page = HomePage(driver)
        assert home_page.is_open() is True, \
            "Не открылась домашняя страница пользователя"

    @allure.title("Логин несуществующего пользователя с корректными данными")
    @allure.description(
        "Тест проверяет, что при вводе корректных электронной почты и пароля "
        "незарегистрированного на сайте пользователя и последующем нажатии на кнопку входа "
        "выводится ошибка с соответствующим текстом"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_fail_when_correct_nonexisting_user(self, driver):
        user = UserFactory.correct_nonexisting_user()

        open_login_page_from_main(driver)
        login_page = login_as(driver, user)

        assert login_page.is_error("Invalid email or password") is True,\
            "Не появилась ошибка о некорректной почте или пароле"

    @allure.title("Логин пользователя с некорректной электронной почтой")
    @allure.description(
        "Тест проверяет, что при вводе некорректной электронной почты и корректного пароля "
        "и последующем наведении курсора мыши на кнопку входа "
        "в тултипе кнопки появляется ошибка с соответствующим текстом"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_fail_when_user_with_incorrect_email(self, driver):
        user = UserFactory.user_with_incorrect_email()

        login_page = open_login_page(driver)
        login_page.enter_credentials(user)
        login_page.hover_signin()

        assert login_page.is_error(
            "Email should be in a correct format") is True, \
            "Не появилась ошибка о некорректной почте"

    @allure.title("Логин пользователя с некорректным паролем")
    @allure.description(
        "Тест проверяет, что при вводе некорректного пароля и корректной электронной почты "
        "и последующем нажатии и наведении курсора мыши на кнопку входа "
        "в тултипе кнопки появляется ошибка с соответствующим текстом"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_fail_when_user_with_incorrect_password(self, driver):
        user = UserFactory.user_with_incorrect_password()

        login_page = open_login_page(driver)
        login_page.enter_credentials(user)
        login_page.press_signin()
        login_page.hover_signin()

        assert login_page.is_error(
            "Password should contain a minimum of 8 characters") is True, \
            "Не появилась ошибка о некорректном пароле"


def open_login_page_from_main(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_login_tab()
    main_page.switch_tab(LoginPage.PAGE_TITLE)

    return LoginPage(driver)

def open_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()

    return login_page

def login_as(driver, user):
    login_page = LoginPage(driver)
    login_page.login_as(user)

    return login_page
