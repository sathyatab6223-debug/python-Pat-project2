import allure
from pages.login_page import LoginPage
from config.config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)


@allure.feature("Login Page UI")
@allure.story("TC03 - Login Field Visibility")
class TestLoginFields:

    @allure.title("Username field should be visible and enabled")
    def test_username_field_visible_and_enabled(self, driver):
        with allure.step("Navigate to login page"):
            driver.get(BASE_URL)

        login_page = LoginPage(driver)

        with allure.step("Verify username field is visible"):
            assert login_page.is_username_field_visible(), \
                "Username input field is NOT visible on the login page"
            logger.info("TC03 | Username field is visible")

        with allure.step("Verify username field is enabled"):
            assert login_page.is_username_field_enabled(), \
                "Username input field is NOT enabled (interactive)"
            logger.info("TC03 | Username field is enabled")

    @allure.title("Password field should be visible and enabled")
    def test_password_field_visible_and_enabled(self, driver):
        with allure.step("Navigate to login page"):
            driver.get(BASE_URL)

        login_page = LoginPage(driver)

        with allure.step("Verify password field is visible"):
            assert login_page.is_password_field_visible(), \
                "Password input field is NOT visible on the login page"
            logger.info("TC03 | Password field is visible")

        with allure.step("Verify password field is enabled"):
            assert login_page.is_password_field_enabled(), \
                "Password input field is NOT enabled (interactive)"
            logger.info("TC03 | Password field is enabled")
