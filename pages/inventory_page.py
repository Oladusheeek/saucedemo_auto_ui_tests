import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage

class InventoryPage(BasePage):

    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    PRICE_ELEMENTS = (By.CLASS_NAME, "inventory_item_price")
    NAME_ELEMENTS = (By.CLASS_NAME, "inventory_item_name")

    ADD_TO_CART_BUTTON_TEMPLATE = "add-to-cart-{item_name}"
    REMOVE_BUTTON_TEMPLATE = "remove-{item_name}"

    PAGE_LOAD_LOCATOR = NAME_ELEMENTS

    @allure.step("Picking sort option: {sort_value}")
    def pick_sort_option(self, sort_value):
        first_item_before_sort = self.find_element(self.PRICE_ELEMENTS)
        dropdown_element = self.find_element(self.FILTER_DROPDOWN)
        Select(dropdown_element).select_by_value(sort_value)
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(first_item_before_sort)
        )

    @allure.step("InventoryPage: Getting all prices")
    def get_all_prices(self):
        prices_web = self.find_elements(self.PRICE_ELEMENTS)
        prices = []
        for element in prices_web: # cut dollar sign and convert to float
            prices.append(self._element_to_float(element))
        
        return prices
    
    @allure.step("InventoryPage: Getting all names")
    def get_all_names_items(self):
        names_web = self.find_elements(self.NAME_ELEMENTS)
        names_of_items = []
        for element in names_web:
            raw_text = element.text
            names_of_items.append(raw_text)
        
        return names_of_items
    
    @allure.step("InventoryPage: getting all items")
    def get_all_items(self):
        item_name = self.get_all_names_items()
        item_price = self.get_all_prices()

        all_items = list(zip(item_name, item_price))
        return all_items
    
    @allure.step("InventoryPage: Adding item to cart: {item_name}")
    def add_item_to_cart_dynamic(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        self.click_element(locator)

    @allure.step("InventoryPage: clicking item_title of item: {item_name}")
    def click_item_title(self, item_name):
        locator = (By.XPATH, f"//div[text()='{item_name}']")
        self.click_element(locator)

    @allure.step("InventoryPage: getting text from add button of item: {item_name}")
    def get_text_add_button(self, item_name):
        dynamic_id = self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        return self.get_text(locator)

    @allure.step("InventoryPage: Removing item {item_name} from cart")
    def remove_item_from_cart_dynamic(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        self.click_element(locator)

    @allure.step("InventoryPage: getting text from remove button of item: {item_name}")
    def get_text_remove_button(self, item_name):
        dynamic_id = self.REMOVE_BUTTON_TEMPLATE.format(item_name=item_name)
        locator = (By.ID, dynamic_id)

        return self.get_text(locator)