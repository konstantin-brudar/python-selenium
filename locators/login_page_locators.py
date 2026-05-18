from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SIGNIN_BUTTON = (By.XPATH, "//button[text()='Sign in']")
    ERROR_MESSAGE_PATTERN = (By.XPATH, "//*[text()='{}']")
