import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from utils.wait_helpers import wait_for_element_visible, wait_for_element_clickable
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def find(self, locator):
        return wait_for_element_visible(self.driver, locator)

    def click(self, locator):
        element = wait_for_element_clickable(self.driver, locator)
        logger.debug(f"Clicking: {locator}")
        element.click()

    def type_text(self, locator, text):
        element = wait_for_element_visible(self.driver, locator)
        element.clear()
        logger.debug(f"Typing '{text}' into {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def is_enabled(self, locator):
        try:
            return self.find(locator).is_enabled()
        except Exception:
            return False

    def take_screenshot(self, name):
        return self.driver.get_screenshot_as_png()
