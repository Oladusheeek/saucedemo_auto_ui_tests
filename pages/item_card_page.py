import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ItemCardPage(BasePage):

    NAME_LOCATOR = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRICE_LOCATOR = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-test="add-to-cart"]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[data-test="remove"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '[data-test="back-to-products"]')

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

    def get_text_remove_button(self):
        return self.get_text(self.REMOVE_BUTTON)
    
    def get_text_add_button(self):
        return self.get_text(self.ADD_TO_CART_BUTTON)