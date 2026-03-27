import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

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
            EC.element_to_be_clickable(locator)
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