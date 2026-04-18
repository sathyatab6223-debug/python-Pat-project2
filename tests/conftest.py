import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config.config import BASE_URL, BROWSER
from utils.logger import get_logger

logger = get_logger(__name__)


def _build_driver():
    browser = BROWSER.lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Choose chrome, firefox, or edge.")

    logger.info(f"Browser launched: {browser.upper()}")
    return driver


@pytest.fixture(scope="function")
def driver():
    drv = _build_driver()
    drv.get(BASE_URL)
    logger.info(f"Navigated to base URL: {BASE_URL}")
    yield drv
    logger.info("Closing browser")
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            try:
                screenshot = drv.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG,
                )
                logger.warning(f"Screenshot captured for failed test: {item.nodeid}")
            except Exception as exc:
                logger.error(f"Failed to capture screenshot: {exc}")
