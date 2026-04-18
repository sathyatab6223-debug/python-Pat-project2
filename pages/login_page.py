from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):

    USERNAME_INPUT       = (By.NAME, "username")
    PASSWORD_INPUT       = (By.NAME, "password")
    LOGIN_BUTTON         = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE        = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(@class,'orangehrm-login-forgot')]")
    RESET_USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    RESET_SUBMIT_BUTTON  = (By.XPATH, "//button[@type='submit']")
    RESET_CONFIRMATION   = (By.XPATH, "//h6 | //p[contains(@class,'orangehrm-forgot-password')]")

    def enter_username(self, username):
        logger.info(f"Entering username: '{username}'")
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        logger.info("Entering password")
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        logger.info("Clicking Login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_username_field_visible(self):
        return self.is_displayed(self.USERNAME_INPUT)

    def is_password_field_visible(self):
        return self.is_displayed(self.PASSWORD_INPUT)

    def is_username_field_enabled(self):
        return self.is_enabled(self.USERNAME_INPUT)

    def is_password_field_enabled(self):
        return self.is_enabled(self.PASSWORD_INPUT)

    def click_forgot_password(self):
        logger.info("Clicking 'Forgot your password?' link")
        element = self.find(self.FORGOT_PASSWORD_LINK)
        element.click()

    def submit_reset_request(self, username):
        logger.info(f"Submitting password reset for username: '{username}'")
        self.type_text(self.RESET_USERNAME_INPUT, username)
        self.click(self.RESET_SUBMIT_BUTTON)

    def get_reset_confirmation_text(self):
        return self.get_text(self.RESET_CONFIRMATION)
