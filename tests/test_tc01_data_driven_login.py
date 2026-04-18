import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.excel_reader import read_login_data
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, TEST_DATA_FILE, LOGIN_SHEET
from utils.logger import get_logger

logger = get_logger(__name__)

# Load all credential rows from Excel at collection time
_login_rows = read_login_data(TEST_DATA_FILE, LOGIN_SHEET)


@allure.feature("Authentication")
@allure.story("TC01 - Data-Driven Login")
class TestDataDrivenLogin:

    @pytest.mark.parametrize(
        "credentials",
        _login_rows,
        ids=[f"row_{i+1}_{r['username']}" for i, r in enumerate(_login_rows)],
    )
    @allure.title("Login attempt: {credentials}")
    def test_login_with_credentials(self, driver, credentials):
        username        = credentials["username"] or ""
        password        = credentials["password"] or ""
        expected_result = str(credentials["expected_result"]).lower()

        logger.info(
            f"TC01 | username='{username}' | expected='{expected_result}'"
        )

        with allure.step("Open login page"):
            driver.get(BASE_URL)

        login_page = LoginPage(driver)
        home_page  = HomePage(driver)

        with allure.step(f"Enter credentials='{username}'"):
            login_page.login(username, password)

        if expected_result == "pass":
            with allure.step("Verify successful login (dashboard visible)"):
                wait_for_url_contains(driver, "dashboard")
                assert home_page.is_dashboard_visible(), (
                    f"Dashboard not visible after login with valid credentials "
                    f"(username='{username}')"
                )
                logger.info("Login successful — dashboard is visible")

            with allure.step("Logout after successful login"):
                home_page.logout()
                wait_for_url_contains(driver, "login")
                logger.info("Logout successful")

        else:  # expected_result == "fail"
            with allure.step("Verify login is rejected with an error message"):
                try:
                    error_msg = login_page.get_error_message()
                    assert error_msg, (
                        f"Expected an error message for invalid credentials "
                        f"(username='{username}') but got none."
                    )
                    logger.info(f"Login correctly rejected. Error: '{error_msg}'")
                except Exception:
                    # If error element not found but URL still shows login, it's still a fail
                    assert "login" in driver.current_url.lower(), (
                        f"Expected login to fail for username='{username}' but "
                        f"URL changed to: {driver.current_url}"
                    )
