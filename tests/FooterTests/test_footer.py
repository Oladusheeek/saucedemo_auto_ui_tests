import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.footer_element import FooterElements

@allure.feature("Test Footer")
class TestFooter:

    @allure.title("Checking twitter link")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_link_twitter(self, logged_in_browser):
        footer = FooterElements(logged_in_browser)

        original_window = logged_in_browser.current_window_handle

        footer.open_twitter()

        footer.switch_to_new_tab(original_window)

        with allure.step("Checking if URL containts x.com/saucelabs"):
            assert "x.com/saucelabs" in logged_in_browser.current_url.lower()

        footer.close_and_switch_back(original_window)
        
        assert "saucedemo.com" in logged_in_browser.current_url.lower()

    
    @allure.title("Checking facebook link")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_link_facebook(self, logged_in_browser):
        footer = FooterElements(logged_in_browser)

        original_window = logged_in_browser.current_window_handle

        footer.open_facebook()
        footer.switch_to_new_tab(original_window)

        with allure.step("Checking if URL contains facebook.com/saucelabs"):
            assert "facebook.com/saucelabs" in logged_in_browser.current_url.lower()

        footer.close_and_switch_back(original_window)

        assert "saucedemo.com" in logged_in_browser.current_url.lower()

    
    @allure.title("Checking linkedin link")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_link_linkedin(self, logged_in_browser):
        footer = FooterElements(logged_in_browser)

        original_window = logged_in_browser.current_window_handle

        footer.open_linkedin()
        footer.switch_to_new_tab(original_window)

        with allure.step("Checking if URL contains linkedin.com/company/sauce-labs"):
            assert "linkedin.com/company/sauce-labs" in logged_in_browser.current_url.lower()

        footer.close_and_switch_back(original_window)

        assert "saucedemo.com" in logged_in_browser.current_url.lower()