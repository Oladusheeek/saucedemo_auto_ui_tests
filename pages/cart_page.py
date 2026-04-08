import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):

    GO_BACK_BUTTON = (By.CSS_SELECTOR, '[data-test="continue-shopping"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

    NAME_ELEMENTS = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRICE_ELEMENTS = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')

    PAGE_LOAD_LOCATOR = CHECKOUT_BUTTON

    @allure.step("Cart: Getting all names")
    def get_all_names_in_cart(self):
        names_web = self.find_elements(self.NAME_ELEMENTS)
        names = []
        for item in names_web:
            names.append(item.text)

        return names
    
    @allure.step("Cart: getting all prices")
    def get_all_prices_in_cart(self):
        prices_web = self.find_elements(self.PRICE_ELEMENTS)
        prices = []
        for item in prices_web:
            prices.append(self._element_to_float(item))

        return prices
    
    @allure.step("Clicking checkout button")
    def click_checkout_button(self):
        self.click_element(self.CHECKOUT_BUTTON)