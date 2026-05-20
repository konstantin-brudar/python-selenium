import allure
import pytest

from config import MAIN_PAGE_URL
from enums.language import Language
from pages.main_page import MainPage


@allure.epic("Сайт Skyrexio")
@allure.feature("Главная страница сайта")
class TestMainPage:

    @allure.title("Перевод кнопки логина на разные языки")
    @allure.description(
        "Тест проверяет, что на разных версиях сайта "
        "кнопка логина переведена правильно"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("language, translation", [
        (Language.EN, "Login"),
        (Language.RU, "Войти"),
        (Language.ES, "Iniciar sesión"),
        (Language.PT, "Entrar"),
    ])
    def test_login_button_translation(self, driver, language, translation):
        url = MAIN_PAGE_URL + language.value

        main_page = MainPage(driver)
        main_page.open(url)

        assert main_page.get_login_button_text() == translation, \
            "Неправильный перевод текста кнопки логина"
