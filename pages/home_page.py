from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN    = (By.XPATH, "//li[contains(@class,'oxd-userdropdown')]")
    LOGOUT_OPTION    = (By.XPATH, "//a[text()='Logout']")

    MENU_ADMIN       = (By.XPATH, "//a[contains(@href,'viewAdminModule')]")
    MENU_PIM         = (By.XPATH, "//span[normalize-space()='PIM']")
    MENU_LEAVE       = (By.XPATH, "//span[text()='Leave']")
    MENU_TIME        = (By.XPATH, "//span[text()='Time']")
    MENU_RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MENU_MY_INFO     = (By.XPATH, "//span[normalize-space()='My Info']")
    MENU_PERFORMANCE = (By.XPATH, "//span[text()='Performance']")
    MENU_DASHBOARD   = (By.XPATH, "//span[text()='Dashboard']")

    ALL_MENU_LOCATORS = {
        "Admin":       MENU_ADMIN,
        "PIM":         MENU_PIM,
        "Leave":       MENU_LEAVE,
        "Time":        MENU_TIME,
        "Recruitment": MENU_RECRUITMENT,
        "My Info":     MENU_MY_INFO,
        "Performance": MENU_PERFORMANCE,
        "Dashboard":   MENU_DASHBOARD,
    }

    def is_dashboard_visible(self):
        return self.is_displayed(self.DASHBOARD_HEADER)

    def logout(self):
        logger.info("Logging out")
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)

    def is_menu_item_visible(self, menu_name):
        locator = self.ALL_MENU_LOCATORS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown menu item: '{menu_name}'")
        return self.is_displayed(locator)

    def is_menu_item_clickable(self, menu_name):
        locator = self.ALL_MENU_LOCATORS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown menu item: '{menu_name}'")
        try:
            from utils.wait_helpers import wait_for_element_clickable
            wait_for_element_clickable(self.driver, locator)
            return True
        except Exception:
            return False

    def click_menu(self, menu_name):
        locator = self.ALL_MENU_LOCATORS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown menu item: '{menu_name}'")
        logger.info(f"Clicking menu: '{menu_name}'")
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
