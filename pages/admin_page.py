import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class AdminPage(BasePage):

    ADD_USER_BUTTON       = (By.XPATH, "//button[normalize-space()='Add']")
    USER_ROLE_DROPDOWN    = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
    EMPLOYEE_NAME_INPUT   = (By.XPATH, "//input[@placeholder='Type for hints...']")
    STATUS_DROPDOWN       = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
    USERNAME_INPUT        = (By.XPATH, "//label[text()='Username']/following::input[1]")
    PASSWORD_INPUT        = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD_INPUT= (By.XPATH, "(//input[@type='password'])[2]")
    SAVE_BUTTON           = (By.XPATH, "//button[@type='submit']")

    SEARCH_USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/following::input[1]")
    SEARCH_BUTTON         = (By.XPATH, "//button[@type='submit']")
    SEARCH_RESULT_ROW     = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    RESULT_USERNAME_CELL  = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][2]")

    @staticmethod
    def _option_locator(text):
        return (By.XPATH, f"//span[text()='{text}']")

    def click_add(self):
        logger.info("Clicking 'Add' user button")
        self.click(self.ADD_USER_BUTTON)

    def select_user_role(self, role):
        logger.info(f"Selecting user role: '{role}'")
        self.click(self.USER_ROLE_DROPDOWN)
        self.click(self._option_locator(role))

    def enter_employee_name(self, name):
        logger.info(f"Entering employee name: '{name}'")
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

    def select_status(self, status):
        logger.info(f"Selecting status: '{status}'")
        self.click(self.STATUS_DROPDOWN)
        self.click(self._option_locator(status))

    def enter_username(self, username):
        logger.info(f"Entering username: '{username}'")
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        logger.info("Entering password for new user")
        self.type_text(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, password):
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)

    def save_user(self):
        logger.info("Saving new user")
        self.click(self.SAVE_BUTTON)

    def add_new_user(self, role, employee_name, status, username, password):
        self.click_add()
        self.select_user_role(role)
        self.enter_employee_name(employee_name)
        self.select_status(status)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.save_user()

    def search_user(self, username):
        logger.info(f"Searching for user: '{username}'")
        self.type_text(self.SEARCH_USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON)

    def get_search_result_username(self):
        return self.get_text(self.RESULT_USERNAME_CELL)

    def has_search_results(self):
        try:
            elements = self.driver.find_elements(*self.SEARCH_RESULT_ROW)
            return len(elements) > 0
        except Exception:
            return False
