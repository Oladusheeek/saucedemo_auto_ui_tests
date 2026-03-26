import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_filter_lohi(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.pick_sort_option("lohi")
    actual_prices = inventory_page.get_all_prices()
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices

def test_filter_hilo(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.pick_sort_option("hilo")
    actual_prices = inventory_page.get_all_prices()
    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices

def test_filter_AZ(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.pick_sort_option("az")
    actual_names = inventory_page.get_all_names_items()
    expected_names = sorted(actual_names)

    assert actual_names == expected_names

def test_filter_ZA(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)
    inventory_page.pick_sort_option("za")
    actual_names = inventory_page.get_all_names_items()
    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names
