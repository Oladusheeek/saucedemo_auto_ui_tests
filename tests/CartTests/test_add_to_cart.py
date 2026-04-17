import pytest, allure

from utility_funcs.load_data import load_data_json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_add_to_cart(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)

    inventory_names = inventory_page.get_all_names_items()
    inventory_prices = inventory_page.get_all_prices()
    all_inventory_items = list(zip(inventory_names, inventory_prices))

    expected_items = all_inventory_items[:3]
    for item_name, item_price in expected_items:
        locator = inventory_page._item_name_to_locator(item_name)
        inventory_page.add_item_to_cart_dynamic(locator)

    with allure.step(f"Open cart page"):
        inventory_page.open_cart()

    cart_page = CartPage(logged_in_browser)
    cart_names = cart_page.get_all_names_in_cart()
    cart_prices = cart_page.get_all_prices_in_cart()
    all_cart_items = list(zip(cart_names, cart_prices))

    with allure.step("Check if items in cart are the ones that were picked in inventory"):
        assert expected_items == all_cart_items
