import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

@pytest.fixture
def browser():
    options = Options()

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    options.add_argument("--disable-features=SafeBrowsing")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_browser(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.login_user("standard_user", "secret_sauce")

    WebDriverWait(browser, 5).until(EC.url_contains("inventory"))

    yield browser

    browser.delete_all_cookies()