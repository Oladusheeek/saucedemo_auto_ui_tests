import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.inventory_page import InventoryPage

def test_change_of_add_button_to_remove(logged_in_browser):
    item_name = "sauce-labs-backpack"
    inventory_page = InventoryPage(logged_in_browser)

    inventory_page.add_item_to_cart_dynamic(item_name)

    assert inventory_page.get_text_remove_button(item_name) == "Remove"
