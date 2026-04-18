# config.py — Central configuration for OrangeHRM test automation

# Application URL
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Admin credentials (used for most test cases)
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

# Browser to use: "chrome" | "firefox" | "edge"
BROWSER = "chrome"

# Explicit wait timeout (seconds)
EXPLICIT_WAIT = 15

# Path to the Excel test data file (relative to project root)
TEST_DATA_FILE = "data/login_data.xlsx"
LOGIN_SHEET = "LoginData"

# Path for log file output
LOG_FILE = "logs/test_execution.log"
