import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver)
    page.open("https://google.com")
    time.sleep(10)
