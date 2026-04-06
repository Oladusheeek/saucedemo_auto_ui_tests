import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    PAGE_LOAD_LOCATOR = None
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