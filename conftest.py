import pytest, allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
from dotenv import load_dotenv
load_dotenv()

from pages.login_page import LoginPage

from constants.constants import Users

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
        default=os.getenv("BASE_URL", "https://www.saucedemo.com/")
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()

        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        options.add_argument("--incognito")
        options.add_argument("--disable-features=SafeBrowsing, PasswordLeakDetection")
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
def logged_in_browser(browser, base_url, request):

    username = getattr(request, "param", Users.STANDARD)

    browser.get(base_url)
    login_page = LoginPage(browser)

    password = os.getenv("SAUCE_PASSWORD")
    if not password:
        raise ValueError("Password not found! Check environment")
    login_page.login_user(username, password)

    WebDriverWait(browser, 5).until(EC.url_contains("inventory"))

    yield browser

    browser.delete_all_cookies()
    browser.execute_script("window.localStorage.clear();")
    browser.execute_script("window.sessionStorage.clear();")



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call): # screenshot on test failure
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == 'call' and rep.failed: # only on stage 'call' and only if test have failed
        driver = None
        browser_fixtures = ['browser', 'logged_in_browser', ] #list of fixtures that can be used in tests
        for fixture_name in browser_fixtures:
            if fixture_name in item.funcargs:
                driver = item.funcargs[fixture_name]
                break
            
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_of_error_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to make screenshot:  {e}")