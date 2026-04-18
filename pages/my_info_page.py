from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class MyInfoPage(BasePage):

    MENU_PERSONAL_DETAILS   = (By.XPATH, "//a[text()='Personal Details']")
    MENU_CONTACT_DETAILS    = (By.XPATH, "//a[text()='Contact Details']")
    MENU_EMERGENCY_CONTACTS = (By.XPATH, "//a[text()='Emergency Contacts']")
    MENU_DEPENDENTS         = (By.XPATH, "//a[text()='Dependents']")
    MENU_IMMIGRATION        = (By.XPATH, "//a[text()='Immigration']")
    MENU_JOB                = (By.XPATH, "//a[text()='Job']")
    MENU_SALARY             = (By.XPATH, "//a[text()='Salary']")
    MENU_TAX_EXEMPTIONS     = (By.XPATH, "//a[text()='Tax Exemptions']")
    MENU_REPORT_TO          = (By.XPATH, "//a[text()='Report-to']")
    MENU_QUALIFICATIONS     = (By.XPATH, "//a[text()='Qualifications']")
    MENU_MEMBERSHIPS        = (By.XPATH, "//a[text()='Memberships']")

    SUB_MENUS = {
        "Personal Details":   MENU_PERSONAL_DETAILS,
        "Contact Details":    MENU_CONTACT_DETAILS,
        "Emergency Contacts": MENU_EMERGENCY_CONTACTS,
        "Dependents":         MENU_DEPENDENTS,
        "Immigration":        MENU_IMMIGRATION,
        "Job":                MENU_JOB,
        "Salary":             MENU_SALARY,
        "Tax Exemptions":     MENU_TAX_EXEMPTIONS,
        "Report-to":          MENU_REPORT_TO,
        "Qualifications":     MENU_QUALIFICATIONS,
        "Memberships":        MENU_MEMBERSHIPS,
    }

    def is_sub_menu_visible(self, menu_name):
        locator = self.SUB_MENUS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown My Info sub-menu: '{menu_name}'")
        return self.is_displayed(locator)

    def click_sub_menu(self, menu_name):
        locator = self.SUB_MENUS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown My Info sub-menu: '{menu_name}'")
        logger.info(f"Clicking My Info sub-menu: '{menu_name}'")
        self.click(locator)

    def is_sub_menu_clickable(self, menu_name):
        locator = self.SUB_MENUS.get(menu_name)
        if not locator:
            raise ValueError(f"Unknown My Info sub-menu: '{menu_name}'")
        try:
            from utils.wait_helpers import wait_for_element_clickable
            wait_for_element_clickable(self.driver, locator)
            return True
        except Exception:
            return False
