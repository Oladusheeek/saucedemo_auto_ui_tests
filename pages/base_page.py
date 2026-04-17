import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from typing import Optional

class BasePage:
    PAGE_LOAD_LOCATOR = None

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CLOSE_BURGER_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    RESET_APP_STATE_BUTTON = (By.CSS_SELECTOR, '[data-test="reset-sidebar-link"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')

    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10))

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_page_load()

    @allure.step("Waiting for page to load")
    def wait_for_page_load(self) -> None:
        if self.PAGE_LOAD_LOCATOR:
            WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(self.PAGE_LOAD_LOCATOR),message=f"Page {self.__class__.__name__} did not load! Locator {self.PAGE_LOAD_LOCATOR} was not found!"
            )

    @allure.step("Opening page: {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Finding element with locator: {locator}")
    def find_element(self, locator: tuple, timeout: Optional[int]=None) -> WebElement:
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Finding elementS with locator: {locator}")
    def find_elements(self, locator: tuple, timeout: Optional[int]=None) -> list[WebElement]:
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    
    @allure.step("Clicking element: {locator}")
    def click_element(self, locator: tuple, timeout: Optional[int]=None) -> None:
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Cant click on {locator}"
        ).click()

    @allure.step("Entering text: {text} to locator: {locator}")
    def enter_text(self, locator: tuple, text: str, timeout: Optional[int]=None) -> None:
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(text)

    @allure.step("Getting text from: {locator}")
    def get_text(self, locator: tuple, timeout: Optional[int]=None) -> str:
        web_element = self.find_element(locator, timeout=timeout)
        return web_element.text
    
    @allure.step("Converting web element to float")
    def _element_to_float(self, price_element: WebElement) -> float:
            raw_text = price_element.text
            clean_text = raw_text.replace("$", "")
            return float(clean_text)
    
    @allure.step("Checking if element is present")
    def is_element_present(self, locator: tuple, timeout: int=0) -> bool:
        if timeout > 0:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            except TimeoutException:
                return False
            
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
    
    @allure.step("Open burger menu")
    def click_burger_menu_button(self) -> None:
        self.click_element(self.BURGER_MENU_BUTTON)

    @allure.step("Click on 'Reset app state' button")
    def reset_app_state(self) -> None:
        self.click_element(self.RESET_APP_STATE_BUTTON)

    @allure.step("Logout")
    def logout(self) -> None:
        self.click_element(self.LOGOUT_BUTTON)

    @allure.step("Opening cart")
    def open_cart(self) -> None:
        self.click_element(self.CART_BUTTON)

    @allure.step("Getting text from cart badge")
    def get_text_from_cart_badge(self) -> str:
        return self.get_text(self.SHOPPING_CART_BADGE)
    
    @allure.step("Checking if cart badge is present")
    def is_cart_badge_present(self) -> bool:
        return self.is_element_present(self.SHOPPING_CART_BADGE)
    
    @allure.step("Waiting for cart_badge to update to: '{expected_text}'")
    def wait_for_cart_badge_to_update(self, expected_text: str, timeout: Optional[int]=None) -> None:
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SHOPPING_CART_BADGE, expected_text),
            message=f"Counter did not update to: {expected_text}"
        )

    @allure.step("Converting item_name {item_name} to locator")
    def _item_name_to_locator(self, item_name: str ) -> str:
        return item_name.lower().replace(" ", "-")