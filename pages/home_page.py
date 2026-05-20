import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    locators = HomePageLocators()
    PAGE_TITLE = "Home"

    @allure.step("Проверка, что открыта домашняя страница")
    def is_open(self):
        return self.title_contains(self.PAGE_TITLE)

    @allure.step("Получение наименования плана")
    def get_plan_name(self):
        elem = self.element_is_visible(self.locators.PLAN_NAME)
        return elem.text

    @allure.step("Получение цвета текста наименования плана")
    def get_plan_name_color(self):
        elem = self.element_is_visible(self.locators.PLAN_NAME)
        return self.get_color(elem)

    @allure.step("Получение даты окончания действия плана")
    def get_finish_date(self):
        elem = self.element_is_visible(self.locators.PLAN_FINISH_DATE)
        return elem.text

    @allure.step("Получение цвета текста даты окончания действия плана")
    def get_finish_date_color(self):
        elem = self.element_is_visible(self.locators.PLAN_FINISH_DATE)
        return self.get_color(elem)
