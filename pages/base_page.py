import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    PAGE_LOAD_LOCATOR = None

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CLOSE_BURGER_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    RESET_APP_STATE_BUTTON = (By.CSS_SELECTOR, '[data-test="reset-sidebar-link"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')


    def __init__(self, driver):
        self.driver = driver
        self.wait_for_page_load()

    def wait_for_page_load(self):
        if self.PAGE_LOAD_LOCATOR:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.PAGE_LOAD_LOCATOR),message=f"Page {self.__class__.__name__} did not load! Locator {self.PAGE_LOAD_LOCATOR} was not found!"
            )

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, timeout=time).until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator)
        )
    
    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, timeout=time).until(
            EC.element_to_be_clickable(locator),
            message=f"Cant click on {locator}"
        ).click()

    def enter_text(self, locator, text, time=10):
        WebDriverWait(self.driver, timeout=time).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(text)

    def get_text(self, locator, time=10):
        web_element = self.find_element(locator, time)
        return web_element.text
    
    def _element_to_float(self, priceString):
            raw_text = priceString.text
            clean_text = raw_text.replace("$", "")
            return float(clean_text)
    
    def is_element_present(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
    
    @allure.step("Open burger menu")
    def click_burger_menu_button(self):
        self.click_element(self.BURGER_MENU_BUTTON)

    @allure.step("Click on 'Reset app state' button")
    def reset_app_state(self):
        self.click_element(self.RESET_APP_STATE_BUTTON)

    @allure.step("Logout")
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    @allure.step("Opening cart")
    def open_cart(self):
        self.click_element(self.CART_BUTTON)

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