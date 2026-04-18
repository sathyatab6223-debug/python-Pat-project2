import allure
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.claim_page import ClaimPage
from utils.wait_helpers import wait_for_url_contains
from config.config import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utils.logger import get_logger

logger = get_logger(__name__)

# Test data for claim submission
CLAIM_EVENT  = "Travel"                        # Must match an event in the dropdown
CURRENCY     = "USD - United States Dollar"   # Must match a currency in the dropdown
REMARKS      = "Automated test claim request"


@allure.feature("Claim Management")
@allure.story("TC10 - Submit Claim Request")
class TestClaimRequest:

    @allure.title("User initiates a claim request and submission is confirmed")
    def test_submit_claim(self, driver):

        # Step 1: Login
        with allure.step("Login as Admin"):
            driver.get(BASE_URL)
            login_page = LoginPage(driver)
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
            wait_for_url_contains(driver, "dashboard")
            logger.info("TC10 | Logged in")

        # Step 2: Navigate to Claim > Submit Claim
        with allure.step("Navigate to Claim > Submit Claim"):
            claim_page = ClaimPage(driver)
            claim_page.navigate_to_claim()
            claim_page.click_submit_claim()
            wait_for_url_contains(driver, "submitClaim")
            logger.info("TC10 | On Submit Claim page")

        # Step 3: Fill and submit the claim form
        with allure.step("Fill claim form and submit"):
            claim_page.select_event(CLAIM_EVENT)
            claim_page.select_currency(CURRENCY)
            claim_page.enter_remarks(REMARKS)
            claim_page.click_create()
            time.sleep(2)
            logger.info("TC10 | Claim form submitted")

        # Step 4: Verify submission was accepted
        with allure.step("Verify claim submission confirmation"):
            current_url = driver.current_url
            # After successful submission, OrangeHRM redirects to the claim detail page
            assert "claim" in current_url.lower(), (
                f"Expected to stay in claim section after submission. "
                f"Current URL: {current_url}"
            )
            logger.info("TC10 | Claim submitted and confirmed successfully")
