import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.my_info_page import MyInfoPage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

EXPECTED_SUB_MENUS = [
    "Personal Details",
    "Contact Details",
    "Emergency Contacts",
    "Dependents",
    "Immigration",
    "Job",
    "Salary",
    "Report-to",
    "Qualifications",
    "Memberships",
]


@allure.feature("My Info")
@allure.story("TC08 - My Info Sub-Menu Presence")
class TestMyInfoMenu:

    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        wait_for_url_contains(driver, "dashboard")

        home_page = HomePage(driver)
        home_page.click_menu("My Info")
        wait_for_url_contains(driver, "viewPersonalDetails")
        self.my_info = MyInfoPage(driver)

    @pytest.mark.parametrize("menu_name", EXPECTED_SUB_MENUS)
    @allure.title("My Info sub-menu '{menu_name}' should be visible and clickable")
    def test_sub_menu_visible_and_clickable(self, driver, menu_name):
        with allure.step(f"Check visibility: '{menu_name}'"):
            assert self.my_info.is_sub_menu_visible(menu_name), (
                f"My Info sub-menu '{menu_name}' is NOT visible"
            )
            logger.info(f"TC08 | '{menu_name}' is visible")

        with allure.step(f"Check clickability: '{menu_name}'"):
            assert self.my_info.is_sub_menu_clickable(menu_name), (
                f"My Info sub-menu '{menu_name}' is NOT clickable"
            )
            logger.info(f"TC08 | '{menu_name}' is clickable")
