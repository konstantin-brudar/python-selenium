from selenium.webdriver.common.by import By


class HomePageLocators:
    PLAN_NAME = (By.XPATH, "//div[h3[text()='Plan']]/div/span[1]")
    PLAN_FINISH_DATE = (By.XPATH, "//div[h3[text()='Plan']]/div/span[last()]")
