import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        help="specify the browser"
    )
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("base-url")

@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()

        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        options.add_argument("--disable-features=SafeBrowsing")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")
    
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_browser(browser, base_url):
    login_page = LoginPage(browser)

    login_page.open(base_url)
    login_page.login_user("standard_user", "secret_sauce")

    WebDriverWait(browser, 5).until(EC.url_contains("inventory"))

    yield browser

    browser.delete_all_cookies()