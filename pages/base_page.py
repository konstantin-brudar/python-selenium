


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def open(self, url):
        self.driver.get(url)