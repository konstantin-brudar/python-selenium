import allure
import pytest

from allure_commons.types import AttachmentType
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config import BROWSER_WIDTH, BROWSER_HEIGHT, DEFAULT_TIMEOUT


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер: chrome или firefox"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser").lower()

    if browser == "chrome":
        options = ChromeOptions()
        add_options(options, False)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise pytest.UsageError(
            f"--browser должен быть 'chrome' или 'firefox'. Передано: {browser}"
        )

    driver.set_window_size(BROWSER_WIDTH, BROWSER_HEIGHT)
    driver.implicitly_wait(DEFAULT_TIMEOUT)

    yield driver
    driver.quit()

def add_options(options, is_guest_mode=True):
    if is_guest_mode:
        options.add_argument("--guest")
        options.add_argument("--headless")
    else:
        path = Path("~/selenium_profile").expanduser()
        options.add_argument(f"--user-data-dir={path}")
        options.add_argument("--incognito")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failed_test_screenshot",
                attachment_type=AttachmentType.PNG
            )
