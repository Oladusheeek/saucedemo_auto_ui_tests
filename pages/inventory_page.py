import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRICE_ELEMENTS = (By.CLASS_NAME, "inventory_item_price")
    NAME_ELEMENTS = (By.CLASS_NAME, "inventory_item_name")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    ADD_TO_CART_BUTTON_TEMPLATE = "add-to-cart-{item_name}"
    REMOVE_BUTTON_TEMPLATE = "remove-{item_name}"

    def pick_sort_option(self, sort_value):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((self.FILTER_DROPDOWN))
        )
        first_item_before_sort = self.driver.find_element(*self.PRICE_ELEMENTS)
        dropdown_element = self.driver.find_element(*self.FILTER_DROPDOWN)
        Select(dropdown_element).select_by_value(sort_value)
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(first_item_before_sort)
        )

    def get_all_prices(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.PRICE_ELEMENTS)
        )
        prices_web = self.driver.find_elements(*self.PRICE_ELEMENTS)
        prices = []
        for element in prices_web: # cut dollar sign and convert to float
            raw_text = element.text
            clean_text = raw_text.replace("$", "")
            prices.append(float(clean_text))
        
        return prices
    
    def get_all_names_items(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.NAME_ELEMENTS)
        )
        names_web = self.driver.find_elements(*self.NAME_ELEMENTS)
        names_of_items = []
        for element in names_web:
            raw_text = element.text
            names_of_items.append(raw_text)
        
        return names_of_items
    
    def add_item_to_cart_dynamic(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text_add_button(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        return button.text

    def remove_item_from_cart_dynamic(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text_remove_button(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        return button.text

    def get_text_from_cart_badge(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SHOPPING_CART_BADGE)
        )
        text = self.driver.find_element(*self.SHOPPING_CART_BADGE).text
        return text