from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import EXPLICIT_WAIT
from utils.logger import get_logger

logger = get_logger(__name__)


def wait_for_element_visible(driver, locator, timeout=EXPLICIT_WAIT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        logger.debug(f"Element visible: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timeout: element not visible after {timeout}s — {locator}")
        raise


def wait_for_element_clickable(driver, locator, timeout=EXPLICIT_WAIT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        logger.debug(f"Element clickable: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timeout: element not clickable after {timeout}s — {locator}")
        raise


def wait_for_url_contains(driver, partial_url, timeout=EXPLICIT_WAIT):
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(partial_url))
        logger.debug(f"URL now contains: '{partial_url}'")
    except TimeoutException:
        logger.error(f"Timeout: URL did not contain '{partial_url}' after {timeout}s. Current URL: {driver.current_url}")
        raise


def wait_for_text_in_element(driver, locator, text, timeout=EXPLICIT_WAIT):
    try:
        result = WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
        logger.debug(f"Text '{text}' found in {locator}")
        return result
    except TimeoutException:
        logger.error(f"Timeout: text '{text}' not found in {locator} after {timeout}s")
        raise


def wait_for_element_present(driver, locator, timeout=EXPLICIT_WAIT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        logger.debug(f"Element present in DOM: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timeout: element not in DOM after {timeout}s — {locator}")
        raise
