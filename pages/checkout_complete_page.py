import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):

    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, '[data-test="back-to-products"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    PAGE_LOAD_LOCATOR = BACK_TO_PRODUCTS_BUTTON

    @allure.step("CheckoutComplete : back to products")
    def click_back_to_products_button(self) -> None:
        self.click_element(self.BACK_TO_PRODUCTS_BUTTON)

    @allure.step("CheckoutComplete : getting text from complete header")
    def get_text_from_complete_header(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)