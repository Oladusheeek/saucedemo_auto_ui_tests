import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CheckoutStepOnePage(BasePage):

    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, '[data-test="postalCode"]')

    PAGE_LOAD_LOCATOR = CONTINUE_BUTTON

    @allure.step("CheckoutStepOne : filling first name field")
    def fill_first_name_field(self, first_name):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)

    @allure.step("CheckoutStepOne : filling last name field")
    def fill_last_name_field(self, last_name):
        self.enter_text(self.LAST_NAME_FIELD, last_name)

    @allure.step("CheckoutStepOne : filling postal code field")
    def fill_postal_code_field(self, postal_code):
        self.enter_text(self.POSTAL_CODE_FIELD, postal_code)

    @allure.step("CheckoutStepOne : fiiling form with data {first_name}, {last_name}, {postal_code}")
    def fill_form(self, first_name, last_name, postal_code):
        self.fill_first_name_field(first_name=first_name)
        self.fill_last_name_field(last_name=last_name)
        self.fill_postal_code_field(postal_code=postal_code)

    @allure.step("CheckoutStepOne : click cancel button")
    def click_cancel(self):
        self.click_element(self.CANCEL_BUTTON)

    @allure.step("CheckoutStepOne : click continue button")
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    