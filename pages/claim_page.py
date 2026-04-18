from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class ClaimPage(BasePage):

    CLAIM_MENU_ITEM      = (By.XPATH, "//span[text()='Claim']")
    SUBMIT_CLAIM_LINK    = (By.XPATH, "//a[text()='Submit Claim']")
    EVENT_DROPDOWN       = (By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[1]")
    CURRENCY_DROPDOWN    = (By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[2]")
    REMARKS_INPUT        = (By.XPATH, "//textarea")
    CREATE_BUTTON        = (By.XPATH, "//button[@type='submit']")
    SUCCESS_HEADER       = (By.XPATH, "//h6[contains(@class,'oxd-text')]")
    FIRST_DROPDOWN_OPTION= (By.XPATH, "//div[@role='listbox']//div[@role='option'][2]//span")

    def navigate_to_claim(self):
        logger.info("Navigating to Claim module")
        self.click(self.CLAIM_MENU_ITEM)

    def click_submit_claim(self):
        logger.info("Clicking Submit Claim")
        self.click(self.SUBMIT_CLAIM_LINK)

    def select_event(self, event):
        logger.info(f"Selecting claim event: '{event}'")
        self.click(self.EVENT_DROPDOWN)
        self.click(self.FIRST_DROPDOWN_OPTION)

    def select_currency(self, currency):
        logger.info(f"Selecting currency: '{currency}'")
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.FIRST_DROPDOWN_OPTION)

    def enter_remarks(self, remarks):
        logger.info(f"Entering remarks: '{remarks}'")
        self.type_text(self.REMARKS_INPUT, remarks)

    def click_create(self):
        logger.info("Submitting claim request")
        self.click(self.CREATE_BUTTON)

    def get_page_header(self):
        return self.get_text(self.SUCCESS_HEADER)

    def submit_claim(self, event, currency, remarks):
        self.navigate_to_claim()
        self.click_submit_claim()
        self.select_event(event)
        self.select_currency(currency)
        self.enter_remarks(remarks)
        self.click_create()
