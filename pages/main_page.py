import allure

from config import MAIN_PAGE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    locators = MainPageLocators()

    @allure.step("Открытие главной страницы сайта")
    def open_page(self):
        self.open(MAIN_PAGE_URL)

    @allure.step("Переход по ссылке на страницу логина")
    def open_login_tab(self):
        login = self.element_is_clickable(self.locators.LOGIN_BUTTON)
        login.click()

    @allure.step("Получение текста кнопки логина")
    def get_login_button_text(self):
        login = self.element_is_visible(self.locators.LOGIN_BUTTON)
        return login.text
