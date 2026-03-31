import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage

class InventoryPage(BasePage):

    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRICE_ELEMENTS = (By.CLASS_NAME, "inventory_item_price")
    NAME_ELEMENTS = (By.CLASS_NAME, "inventory_item_name")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    ADD_TO_CART_BUTTON_TEMPLATE = "add-to-cart-{item_name}"
    REMOVE_BUTTON_TEMPLATE = "remove-{item_name}"

    PAGE_LOAD_LOCATOR = NAME_ELEMENTS

    def pick_sort_option(self, sort_value):
        first_item_before_sort = self.find_element(self.PRICE_ELEMENTS)
        dropdown_element = self.find_element(self.FILTER_DROPDOWN)
        Select(dropdown_element).select_by_value(sort_value)
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(first_item_before_sort)
        )

    def get_all_prices(self):
        prices_web = self.find_elements(self.PRICE_ELEMENTS)
        prices = []
        for element in prices_web: # cut dollar sign and convert to float
            prices.append(self._element_to_float(element))
        
        return prices
    
    def get_all_names_items(self):
        names_web = self.find_elements(self.NAME_ELEMENTS)
        names_of_items = []
        for element in names_web:
            raw_text = element.text
            names_of_items.append(raw_text)
        
        return names_of_items
    
    def add_item_to_cart_dynamic(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        self.click_element(locator)

    def get_text_add_button(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        return self.get_text(locator)

    def remove_item_from_cart_dynamic(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        self.click_element(locator)

    def get_text_remove_button(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        return self.get_text(locator)

    def get_text_from_cart_badge(self):
        return self.get_text(self.SHOPPING_CART_BADGE)

    def open_cart(self):
        self.click_element(self.CART_BUTTON)