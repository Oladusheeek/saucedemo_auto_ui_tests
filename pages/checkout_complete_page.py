from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):

    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, '[data-test="back-to-products"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    PAGE_LOAD_LOCATOR = BACK_TO_PRODUCTS_BUTTON

    def click_back_to_products_button(self):
        self.click_element(self.BACK_TO_PRODUCTS_BUTTON)

    def get_text_from_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)