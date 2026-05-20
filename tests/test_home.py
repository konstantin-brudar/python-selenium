import allure

from data.user_factory import UserFactory
from enums.color import Color
from enums.plan import Plan
from pages.home_page import HomePage
from tests.test_login import open_login_page, login_as


@allure.epic("Сайт Skyrexio")
@allure.feature("Домашняя страница пользователя")
class TestHomePage:

    @allure.title("Проверка наименование плана")
    @allure.description("Тест проверяет, что в карточке плана указано наименование плана basic")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_plan_name(self, driver):
        home_page = open_home_page(driver)

        plan_name = home_page.get_plan_name()

        assert plan_name.lower() == Plan.BASIC.value, f"План не {Plan.BASIC.value}"

    @allure.title("Проверка цвета текста наименования плана")
    @allure.description(
        "Тест проверяет, что в карточке плана "
        "текст наименования плана имеет темный цвет шрифта"
    )
    @allure.severity(allure.severity_level.MINOR)
    def test_plan_name_color(self, driver):
        home_page = open_home_page(driver)

        plan_name_color = home_page.get_plan_name_color()

        assert plan_name_color == Color.DARK_GRAY.value, f"Цвет плана не {Color.DARK_GRAY.value}"

    @allure.title("Проверка даты окончания действия плана")
    @allure.description(
        "Тест проверяет, что в карточке плана "
        "указана дата окончания действия плана lifetime"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_plan_finish_date(self, driver):
        EXPECTED_DATE = "lifetime"
        home_page = open_home_page(driver)

        finish_date = home_page.get_finish_date()

        assert EXPECTED_DATE in finish_date.lower(), \
            f"Дата окончания действия плана не {EXPECTED_DATE}"

    @allure.title("Проверка цвета текста даты окончания действия плана")
    @allure.description(
        "Тест проверяет, что в карточке плана "
        "текст даты окончания действия плана имеет светло-серый цвет шрифта"
    )
    @allure.severity(allure.severity_level.MINOR)
    def test_plan_finish_date_color(self, driver):
        home_page = open_home_page(driver)

        finish_date_color = home_page.get_finish_date_color()

        assert finish_date_color == Color.LIGHT_GRAY.value, \
            f"Цвет даты окончания действия плана не {Color.LIGHT_GRAY.value}"


def open_home_page(driver):
    user = UserFactory.correct_existing_user()
    open_login_page(driver)
    login_as(driver, user)

    return HomePage(driver)
