import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):

    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel"]')
    FINISH_BUTTON = (By.CSS_SELECTOR, '[data-test="finish"]')

    TOTAL_ITEM_COST_LABEL = (By.CSS_SELECTOR, '[data-test="subtotal-label"]')

    NAME_ELEMENTS = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    PRICE_ELEMENTS = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')

    PAGE_LOAD_LOCATOR = FINISH_BUTTON

    @allure.step("CheckoutStepTwo : click cancel button")
    def click_cancel_button(self) -> None:
        self.click_element(self.CANCEL_BUTTON)

    @allure.step("CheckoutStepTwo : click finish button")
    def click_finish_button(self) -> None:
        self.click_element(self.FINISH_BUTTON)

    @allure.step("CheckoutStepTwo : getting total cost")
    def get_total_item_cost(self) -> float:
        raw_text = self.get_text(self.TOTAL_ITEM_COST_LABEL)
        clean_text = raw_text.split("$")[1]

        return float(clean_text)

    @allure.step("CheckoutStepTwo : getting items' names")
    def get_items_names(self) -> list[str]:
        web_elements = self.find_elements(self.NAME_ELEMENTS)
        items_names = []
        for item in web_elements:
            items_names.append(item.text)

        return items_names

    @allure.step("CheckoutStepTwo : getting items' prices")
    def get_items_prices(self) -> list[float]:
        web_elements = self.find_elements(self.PRICE_ELEMENTS)
        items_prices = []
        for item in web_elements:
            items_prices.append(self._element_to_float(item))

        return items_prices
    
    @allure.step("CheckoutStepTwo : calculating sum of items' prices")
    def sum_of_items_prices(self) -> float:
        array_of_prices = self.get_items_prices()
        return sum(array_of_prices)