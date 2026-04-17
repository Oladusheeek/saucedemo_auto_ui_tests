import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_BANNER = (By.CSS_SELECTOR, "[data-test='error']")

    PAGE_LOAD_LOCATOR = LOGIN_BUTTON
    
    @allure.step("LoginPage: Entering username: {username}")
    def enter_username(self, username: str) -> None:
        self.enter_text(self.USERNAME_FIELD, username)

    @allure.step("LoginPage: Entering password")
    def enter_password(self, password: str) -> None:
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("LoginPage: Clicking on login button")
    def click_login_button(self) -> None:
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("LoginPage: Login user: {username}")
    def login_user(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("LoginPage: getting error text")
    def get_error_text(self) -> str:
        return self.get_text(self.ERROR_BANNER)