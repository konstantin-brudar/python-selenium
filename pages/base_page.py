from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import DEFAULT_TIMEOUT


class BasePage:

    TIMEOUT = DEFAULT_TIMEOUT

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait(self, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout)

    def element_is_visible(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.invisibility_of_element(locator))

    def elements_are_visible(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=TIMEOUT):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def title_contains(self, title, timeout=TIMEOUT):
        return self.wait(timeout).until(lambda driver: title in driver.title)

    def hover(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()

    def switch_tab(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title in self.driver.title:
                break

    def get_color(self, element):
        color = element.value_of_css_property("color")
        return Color.from_string(color).hex
