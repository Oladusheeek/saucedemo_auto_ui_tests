import pytest
from pages.login_page import LoginPage
from utility_funcs.load_data import load_data_json

@pytest.mark.parametrize("test_data", load_data_json("login_positive.json"))
def test_login_positive(browser, test_data):
    username = test_data["username"]
    password = test_data["password"]
    expected_url = test_data["expected_url"]

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login_user(username, password)

    assert expected_url in browser.current_url