import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_BANNER = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((self.USERNAME_FIELD))
        )
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.PASSWORD_FIELD))
        )
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login_user(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_BANNER)
        )
        return self.driver.find_element(*self.ERROR_BANNER).text