import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

EXPECTED_MENUS = [
    "Admin", "PIM", "Leave", "Time",
    "Recruitment", "My Info", "Performance", "Dashboard",
]


@allure.feature("Navigation")
@allure.story("TC04 - Main Menu Visibility")
class TestMenuItems:

    @pytest.fixture(autouse=True)
    def login(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        wait_for_url_contains(driver, "dashboard")
        self.home_page = HomePage(driver)

    @pytest.mark.parametrize("menu_name", EXPECTED_MENUS)
    @allure.title("Menu item '{menu_name}' should be visible and clickable")
    def test_menu_item_visible_and_clickable(self, driver, menu_name):
        with allure.step(f"Check visibility of '{menu_name}' menu"):
            is_visible = self.home_page.is_menu_item_visible(menu_name)
            assert is_visible, f"Menu item '{menu_name}' is NOT visible"
            logger.info(f"TC04 | '{menu_name}' is visible")

        with allure.step(f"Check clickability of '{menu_name}' menu"):
            is_clickable = self.home_page.is_menu_item_clickable(menu_name)
            assert is_clickable, f"Menu item '{menu_name}' is NOT clickable"
            logger.info(f"TC04 | '{menu_name}' is clickable")
