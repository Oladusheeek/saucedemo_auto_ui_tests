import pytest
from pages.login_page import LoginPage
from utility_funcs.load_data import load_data_json

class TestLogin:

    @pytest.mark.parametrize("test_data", load_data_json("login_positive.json"))
    def test_login_positive(self, browser, base_url, test_data):
        username = test_data["username"]
        password = test_data["password"]
        expected_url = test_data["expected_url"]

        browser.get(base_url)

        login_page = LoginPage(browser)
        login_page.login_user(username, password)

        assert expected_url in browser.current_url

    @pytest.mark.parametrize("test_data", load_data_json("login_negative.json"))
    def test_login_negative(self, browser, base_url, test_data):
        username = test_data["username"]
        password = test_data["password"]
        error_msg = test_data["error_msg"]

        browser.get(base_url)

        login_page = LoginPage(browser)
        login_page.login_user(username, password)

        assert login_page.get_error_text() == error_msg