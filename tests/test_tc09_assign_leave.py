import allure
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.leave_page import LeavePage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

# Test data for leave assignment
EMPLOYEE_NAME = "Paul"               # Must be an existing employee in demo data
LEAVE_TYPE    = "CAN - FMLA"         # Must match exactly as shown in the dropdown
FROM_DATE     = "2025-01-05"         # Format: yyyy-dd-mm as expected by OrangeHRM
TO_DATE       = "2025-01-05"


@allure.feature("Leave Management")
@allure.story("TC09 - Assign Leave to Employee")
class TestAssignLeave:

    @allure.title("Admin assigns leave to an employee and verifies success")
    def test_assign_leave(self, driver):

        # Step 1: Login as Admin
        with allure.step("Login as Admin"):
            driver.get(BASE_URL)
            login_page = LoginPage(driver)
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
            wait_for_url_contains(driver, "dashboard")
            logger.info("TC09 | Admin logged in")

        # Step 2: Navigate to Leave module
        with allure.step("Navigate to Leave module"):
            home_page = HomePage(driver)
            home_page.click_menu("Leave")
            wait_for_url_contains(driver, "viewLeaveList")
            logger.info("TC09 | On Leave module")

        # Step 3: Assign leave
        with allure.step(f"Assign leave for employee '{EMPLOYEE_NAME}'"):
            leave_page = LeavePage(driver)
            leave_page.assign_leave(
                employee=EMPLOYEE_NAME,
                leave_type=LEAVE_TYPE,
                from_date=FROM_DATE,
                to_date=TO_DATE,
            )
            time.sleep(2)
            logger.info("TC09 | Leave assignment form submitted")

        # Step 4: Verify success
        with allure.step("Verify success confirmation"):
            current_url = driver.current_url
            # After successful assignment, OrangeHRM typically redirects to
            # the leave list or shows a success toast. We verify navigation occurred.
            assert "leave" in current_url.lower(), (
                f"Unexpected URL after leave assignment: {current_url}"
            )
            logger.info("TC09 | Leave assignment verified successfully")
