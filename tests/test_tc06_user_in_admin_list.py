import allure
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

# Must match the username created in TC05 (or any known existing user)
TARGET_USERNAME = "testuser_auto01"


@allure.feature("User Management")
@allure.story("TC06 - User Appears in Admin List")
class TestUserInAdminList:

    @allure.title("Newly created user should appear in Admin > User Management list")
    def test_user_found_in_admin_list(self, driver):

        # Step 1: Login as Admin
        with allure.step("Login as Admin"):
            driver.get(BASE_URL)
            login_page = LoginPage(driver)
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
            wait_for_url_contains(driver, "dashboard")
            logger.info("TC06 | Admin logged in")

        # Step 2: Navigate to Admin > User Management
        with allure.step("Navigate to Admin > User Management"):
            home_page = HomePage(driver)
            home_page.click_menu("Admin")
            wait_for_url_contains(driver, "viewSystemUsers")
            logger.info("TC06 | On User Management page")

        # Step 3: Search for the user
        with allure.step(f"Search for username: '{TARGET_USERNAME}'"):
            admin_page = AdminPage(driver)
            admin_page.search_user(TARGET_USERNAME)
            time.sleep(2)  # Wait for search results to load
            logger.info(f"TC06 | Search submitted for '{TARGET_USERNAME}'")

        # Step 4: Verify user appears in results
        with allure.step("Verify user appears in search results"):
            assert admin_page.has_search_results(), (
                f"No results found for username '{TARGET_USERNAME}' in Admin list"
            )

            result_username = admin_page.get_search_result_username()
            assert TARGET_USERNAME in result_username, (
                f"Expected '{TARGET_USERNAME}' in results but found '{result_username}'"
            )
            logger.info(f"TC06 | User '{TARGET_USERNAME}' found in admin list")
