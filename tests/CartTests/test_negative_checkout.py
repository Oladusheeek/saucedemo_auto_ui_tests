import allure
import pytest
import random

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

@allure.feature("Checkout Process")
class TestNegativeCheckout:

    @allure.title("Trying to make an empty order")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Known Bug: SauceDemo lets the user to make an empty order")
    def test_empty_cart(self, logged_in_browser):
        inventory_page = InventoryPage(logged_in_browser)
        inventory_page.open_cart()

        cart_page = CartPage(logged_in_browser)
        cart_page.click_checkout_button()

        check1_page = CheckoutStepOnePage(logged_in_browser)
        check1_page.fill_form("John", "Doe", "2905015")
        check1_page.click_continue()

        check2_page = CheckoutStepTwoPage(logged_in_browser)
        check2_page.click_finish_button()

        with allure.step("Check if the order was declined by system"):
            check_complete_page = CheckoutCompletePage(logged_in_browser)
            assert check_complete_page.get_text_from_complete_header() != "Thank you for your order!"

    @allure.title("Trying to make an order without filling the form")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_wo_filling_form(self, logged_in_browser):
        inventory_page = InventoryPage(logged_in_browser)
        items = inventory_page.get_all_items()
        actual_items = random.sample(items, 3)

        for item_name, item_price in actual_items:
            locator = inventory_page._item_name_to_locator(item_name)
            inventory_page.add_item_to_cart_dynamic(locator)
        inventory_page.open_cart()

        cart_page = CartPage(logged_in_browser)
        cart_page.click_checkout_button()

        checkstep1_page = CheckoutStepOnePage(logged_in_browser)
        checkstep1_page.fill_form("", "", "")
        checkstep1_page.click_continue()

        with allure.step("Check if error banner had popped"):
            assert checkstep1_page.get_error_text() == "Error: First Name is required"