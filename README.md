# OrangeHRM Automation Testing

Automated test suite for the [OrangeHRM demo application](https://opensource-demo.orangehrmlive.com) built with **Python + Selenium 4 + pytest + Allure Reports**.

---

## Project Structure

```
orangehrm-automation/
├── config/
│   └── config.py               # Central config: URL, credentials, timeouts
├── data/
│   └── login_data.xlsx         # Excel test data for data-driven login (TC01)
├── logs/                       # Runtime log files (git-ignored)
├── pages/                      # Page Object Model layer
│   ├── base_page.py            # Shared driver actions & wait wrappers
│   ├── login_page.py           # Login page interactions
│   ├── home_page.py            # Dashboard & main menu
│   ├── admin_page.py           # Admin > User Management
│   ├── my_info_page.py         # My Info sub-menu
│   ├── leave_page.py           # Leave > Assign Leave
│   └── claim_page.py           # Claim > Submit Claim
├── reports/                    # Allure results (git-ignored)
│   └── allure-results/
├── tests/                      # Test cases
│   ├── conftest.py             # Fixtures: driver setup, screenshot on failure
│   ├── test_tc01_data_driven_login.py
│   ├── test_tc02_home_url.py
│   ├── test_tc03_login_fields.py
│   ├── test_tc04_menu_items.py
│   ├── test_tc05_create_user.py
│   ├── test_tc06_user_in_admin_list.py
│   ├── test_tc07_forgot_password.py
│   ├── test_tc08_my_info_menu.py
│   ├── test_tc09_assign_leave.py
│   └── test_tc10_claim_request.py
├── utils/
│   ├── excel_reader.py         # openpyxl-based Excel data reader
│   ├── logger.py               # Centralized logger (file + console)
│   └── wait_helpers.py         # Reusable explicit wait functions
├── .gitignore
├── pytest.ini                  # pytest + Allure configuration
└── requirements.txt
```

---

## Test Cases

| ID    | Scenario                                           | Type              |
|-------|----------------------------------------------------|-------------------|
| TC01  | Data-driven login with Excel credentials           | Data-Driven       |
| TC02  | Home URL accessibility                             | Smoke             |
| TC03  | Login field visibility and interactivity           | UI Validation     |
| TC04  | Main menu items visible and clickable after login  | Navigation        |
| TC05  | Create new user and validate login                 | E2E               |
| TC06  | New user appears in Admin user list                | CRUD Validation   |
| TC07  | Forgot Password link and reset flow                | UI Flow           |
| TC08  | My Info sub-menu items presence and clickability   | Navigation        |
| TC09  | Assign leave to an employee                        | E2E               |
| TC10  | Initiate a claim request                           | E2E               |

---

## Prerequisites

- Python 3.10+
- Google Chrome (or Firefox / Edge) installed
- [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) installed (`allure` available in PATH)

---

## Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd orangehrm-automation

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

### Run the full suite
```bash
pytest
```

### Run a single test file
```bash
pytest tests/test_tc01_data_driven_login.py
```

### Run with a specific browser (override config at runtime)
Edit `config/config.py` and set `BROWSER = "firefox"` or `"edge"`, then run normally.

---

## Viewing Allure Reports

After running tests:

```bash
allure serve reports/allure-results
```

This opens an interactive report in your default browser showing:
- Pass / Fail / Broken / Skipped summary
- Step-by-step breakdown per test
- Screenshots attached automatically on failure
- Timeline and history views

---

## Architecture Notes

### Page Object Model (POM)
Every page of the application has its own class under `pages/`. Tests import page classes and call their methods — locators never appear in test files.

### Centralized Configuration (`config/config.py`)
All environment constants (URL, credentials, timeouts) are defined once. No magic strings in tests.

### Explicit Waits Only
`utils/wait_helpers.py` provides reusable wait functions (`wait_for_element_visible`, `wait_for_element_clickable`, etc.). `time.sleep()` is used only where dynamic content (autocomplete dropdowns) requires a short settle time.

### Data-Driven Testing
TC01 reads credentials from `data/login_data.xlsx` via `utils/excel_reader.py`. Adding new scenarios requires only a new row in the Excel file — no code changes.

### Logging
Every test action is logged to both the console and `logs/test_execution.log` with timestamps, log levels, and module names for easy debugging.

### Screenshot on Failure
`conftest.py` implements a pytest hook that captures a browser screenshot and attaches it directly to the Allure report whenever a test fails.
