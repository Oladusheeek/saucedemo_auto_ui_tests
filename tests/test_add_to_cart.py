import pytest

from utility_funcs.load_data import load_data_json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("item_name", load_data_json("add_to_cart_data.json"))
def test_add_to_cart(logged_in_browser, item_name):
    actual_item_name = item_name[0]
    invenortyPage = InventoryPage(logged_in_browser)
    invenortyPage.add_item_to_cart_dynamic(actual_item_name)
    
    assert invenortyPage.get_text_from_cart_badge() == "1"