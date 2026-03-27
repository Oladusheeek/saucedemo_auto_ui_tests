import pytest
from pages.login_page import LoginPage
from utility_funcs.load_data import load_data_json

@pytest.mark.parametrize("username, password, error_msg", load_data_json("login_negative.json"))
def test_login_negative(browser, username, password, error_msg):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login_user(username, password)

    assert login_page.get_error_text() == error_msg