import pytest, allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage

class ItemCardPage(BasePage):

    NAME_LOCATOR = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRICE_LOCATOR = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-test="add-to-cart"]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[data-test="remove"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '[data-test="back-to-products"]')

    CART_BUTTON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    BURGER_MENU_BUTTON = (By.CSS_SELECTOR, '[data-test="open-menu"]')

    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    PAGE_LOAD_LOCATOR = ADD_TO_CART_BUTTON

    
    @allure.step("ItemCardPage: Getting name")
    def get_name(self):
        return self.get_text(self.NAME_LOCATOR)

    @allure.step("ItemCardPage: Getting price")
    def get_price(self):
        price_web = self.find_element(self.PRICE_LOCATOR)
        return self._element_to_float(price_web)
    
    @allure.step("ItemCardPage: Adding item to cart")
    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    @allure.step("ItemCardPage: Removing item from cart")
    def remove_from_cart(self):
        self.click_element(self.REMOVE_BUTTON)

    @allure.step("ItemCardPage: Returning to inventory")
    def go_to_inventory(self):
        self.click_element(self.BACK_BUTTON)

    @allure.step("ItemCardPage: Opening cart")
    def open_cart(self):
        self.click_element(self.CART_BUTTON)
    
    @allure.step("ItemCardPage: Opening burger-menu")
    def open_burger_menu(self):
        self.click_element(self.BURGER_MENU_BUTTON)

    def get_text_from_cart_badge(self):
        return self.get_text(self.SHOPPING_CART_BADGE)
    
    def is_cart_badge_present(self):
        return self.is_element_present(self.SHOPPING_CART_BADGE)
    
    @allure.step("Waiting for cart_badge to update to: '{expected_text}'")
    def wait_for_cart_badge_to_update(self, expected_text, time=5):
        WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(self.SHOPPING_CART_BADGE, expected_text),
            message=f"Counter did not update to: {expected_text}"
        )

    def get_text_remove_button(self):
        return self.get_text(self.REMOVE_BUTTON)
    
    def get_text_add_button(self):
        return self.get_text(self.ADD_TO_CART_BUTTON)