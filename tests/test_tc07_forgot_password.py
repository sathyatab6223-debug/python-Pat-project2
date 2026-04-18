import allure
from pages.login_page import LoginPage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME
from utils.logger import get_logger

logger = get_logger(__name__)


@allure.feature("Authentication")
@allure.story("TC07 - Forgot Password Flow")
class TestForgotPassword:

    @allure.title("Forgot Password link should redirect and show confirmation")
    def test_forgot_password_link(self, driver):

        # Step 1: Navigate to login page
        with allure.step("Navigate to login page"):
            driver.get(BASE_URL)
            logger.info("TC07 | On login page")

        login_page = LoginPage(driver)

        # Step 2: Click "Forgot your password?" link
        with allure.step("Click 'Forgot your password?' link"):
            login_page.click_forgot_password()
            wait_for_url_contains(driver, "requestPasswordResetCode")
            logger.info("TC07 | Redirected to password reset page")

        # Step 3: Submit reset request with a registered username
        with allure.step(f"Submit password reset for username '{ADMIN_USERNAME}'"):
            login_page.submit_reset_request(ADMIN_USERNAME)
            logger.info("TC07 | Reset form submitted")

        # Step 4: Verify reset was accepted — page redirects away from the form
        with allure.step("Verify reset confirmation (URL redirected away from form)"):
            import time as _time
            _time.sleep(2)  # Allow redirect / confirmation to render
            current_url = driver.current_url
            # After a successful reset submit, OrangeHRM redirects to a
            # confirmation page — the form URL should no longer be active.
            assert "requestPasswordResetCode" not in current_url or \
                   login_page.is_displayed(login_page.RESET_CONFIRMATION), (
                "Forgot password request was not processed — still on the reset form page"
            )
            logger.info(f"TC07 | Password reset confirmed. Current URL: {current_url}")
