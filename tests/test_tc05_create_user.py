import allure
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

# Credentials for the new user to be created
NEW_USER_USERNAME = "testuser_auto01"
NEW_USER_PASSWORD = "Test@1234!"
EMPLOYEE_NAME     = "Peter Mac Anderson"   # Must match an existing employee in the demo


@allure.feature("User Management")
@allure.story("TC05 - Create New User and Validate Login")
class TestCreateUser:

    @allure.title("Admin creates a new user and the new user can log in")
    def test_create_user_and_login(self, driver):

        # Step 1: Log in as Admin
        with allure.step("Login as Admin"):
            driver.get(BASE_URL)
            login_page = LoginPage(driver)
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
            wait_for_url_contains(driver, "dashboard")
            logger.info("TC05 | Admin logged in")

        # Step 2: Navigate to Admin > User Management and add new user
        with allure.step("Navigate to Admin > User Management"):
            home_page = HomePage(driver)
            home_page.click_menu("Admin")
            wait_for_url_contains(driver, "viewSystemUsers")

        with allure.step(f"Add new user: '{NEW_USER_USERNAME}'"):
            admin_page = AdminPage(driver)
            admin_page.add_new_user(
                role="ESS",
                employee_name=EMPLOYEE_NAME,
                status="Enabled",
                username=NEW_USER_USERNAME,
                password=NEW_USER_PASSWORD,
            )
            time.sleep(2)  # Allow save to complete
            logger.info(f"TC05 | New user '{NEW_USER_USERNAME}' created")

        # Step 3: Logout as Admin
        with allure.step("Admin logs out"):
            home_page.logout()
            wait_for_url_contains(driver, "login")
            logger.info("TC05 | Admin logged out")

        # Step 4: Login as the new user
        with allure.step(f"Login as new user '{NEW_USER_USERNAME}'"):
            login_page.login(NEW_USER_USERNAME, NEW_USER_PASSWORD)
            wait_for_url_contains(driver, "dashboard")
            new_home = HomePage(driver)
            assert new_home.is_dashboard_visible(), (
                f"New user '{NEW_USER_USERNAME}' could not log in — "
                "dashboard not visible"
            )
            logger.info(f"TC05 | New user '{NEW_USER_USERNAME}' logged in successfully")
