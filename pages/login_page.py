import allure
from selenium.common import TimeoutException

from config import LOGIN_PAGE_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    PAGE_TITLE = "Login"

    @allure.step("Открытие страницы логина")
    def open_page(self):
        self.open(LOGIN_PAGE_URL)

    @allure.step("Ввод электронной почты '{email}'")
    def enter_email(self, email):
        elem = self.element_is_visible(self.locators.EMAIL_INPUT)
        elem.click()
        elem.send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        elem = self.element_is_visible(self.locators.PASSWORD_INPUT)
        elem.click()
        elem.send_keys(password)

    @allure.step("Нажатие на кнопку логина")
    def press_signin(self):
        elem = self.element_is_clickable(self.locators.SIGNIN_BUTTON)
        elem.click()

    @allure.step("Наведение курсора мыши на кнопку логина")
    def hover_signin(self):
        elem = self.element_is_visible(self.locators.SIGNIN_BUTTON)
        self.hover(elem)

    @allure.step("Ввод электронной почты и пароля пользователя {user}")
    def enter_credentials(self, user):
        self.enter_email(user.email)
        self.enter_password(user.password)

    @allure.step("Вход на сайт пользователя {user}")
    def login_as(self, user):
        self.enter_credentials(user)
        self.press_signin()

    @allure.step("Определение наличия ошибки с текстом '{message}'")
    def is_error(self, message):
        by, pattern = self.locators.ERROR_MESSAGE_PATTERN
        ERROR_MESSAGE = (by, pattern.format(message))

        try:
            self.element_is_visible(ERROR_MESSAGE)
            return True
        except TimeoutException:
            return False
