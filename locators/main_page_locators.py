from selenium.webdriver.common.by import By

from config import LOGIN_PAGE_URL


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, f"//div/a[@href='{LOGIN_PAGE_URL}']")
