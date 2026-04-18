import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class LeavePage(BasePage):

    ASSIGN_LEAVE_LINK   = (By.XPATH, "//a[text()='Assign Leave']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[1]")
    FROM_DATE_INPUT     = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    TO_DATE_INPUT       = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    ASSIGN_BUTTON       = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST       = (By.XPATH, "//div[contains(@class,'oxd-toast-content')]//p[contains(@class,'oxd-text')]")

    @staticmethod
    def _leave_type_option(leave_type):
        return (By.XPATH, f"//span[text()='{leave_type}']")

    def click_assign_leave(self):
        logger.info("Navigating to Assign Leave")
        self.click(self.ASSIGN_LEAVE_LINK)

    def select_employee(self, name):
        logger.info(f"Selecting employee: '{name}'")
        element = self.find(self.EMPLOYEE_NAME_INPUT)
        element.click()
        for char in name:
            element.send_keys(char)
            time.sleep(0.2)
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        element.send_keys(Keys.ENTER)
        time.sleep(0.5)

    def select_leave_type(self, leave_type):
        logger.info(f"Selecting leave type: '{leave_type}'")
        self.click(self.LEAVE_TYPE_DROPDOWN)
        self.click(self._leave_type_option(leave_type))

    def enter_from_date(self, date):
        self.type_text(self.FROM_DATE_INPUT, date)

    def enter_to_date(self, date):
        self.type_text(self.TO_DATE_INPUT, date)

    def submit_leave(self):
        logger.info("Submitting leave assignment")
        self.click(self.ASSIGN_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_TOAST)

    def assign_leave(self, employee, leave_type,
                     from_date, to_date):
        self.click_assign_leave()
        self.select_employee(employee)
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        self.submit_leave()
