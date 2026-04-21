import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FooterElements(BasePage):
    
    FOOTER_TWITTER = (By.CSS_SELECTOR, '[data-test="social-twitter"]')
    FOOTER_FACEBOOK = (By.CSS_SELECTOR, '[data-test="social-facebook"]')
    FOOTER_LINKEDIN = (By.CSS_SELECTOR, '[data-test="social-linkedin"]')

    @allure.step("Open footer twitter")
    def open_twitter(self) -> None:
        self.scroll_to(self.FOOTER_TWITTER)
        self.click_element(self.FOOTER_TWITTER)

    @allure.step("Open footer facebook")
    def open_facebook(self) -> None:
        self.scroll_to(self.FOOTER_FACEBOOK)
        self.click_element(self.FOOTER_FACEBOOK)

    @allure.step("Open footer linkedin")
    def open_linkedin(self) -> None:
        self.scroll_to(self.FOOTER_LINKEDIN)
        self.click_element(self.FOOTER_LINKEDIN)