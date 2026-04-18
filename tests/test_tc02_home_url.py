import allure
from config.config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)


@allure.feature("Navigation")
@allure.story("TC02 - Home URL Accessibility")
class TestHomeUrl:

    @allure.title("Home URL should load without error")
    def test_home_url_accessible(self, driver):
        with allure.step(f"Navigate to {BASE_URL}"):
            driver.get(BASE_URL)
            current_url = driver.current_url
            title = driver.title
            logger.info(f"TC02 | URL='{current_url}' | Title='{title}'")

        with allure.step("Verify page title is not empty"):
            assert title, "Page title is empty — page may not have loaded"

        with allure.step("Verify URL contains expected path segment"):
            assert "orangehrmlive" in current_url.lower(), (
                f"Unexpected URL after navigation: {current_url}"
            )
            logger.info("TC02 PASSED — Home URL is accessible")
