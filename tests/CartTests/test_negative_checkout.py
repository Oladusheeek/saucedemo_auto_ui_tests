import allure
import pytest
import random

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.item_card_page import ItemCardPage

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

    @allure.title("Removing item from CheckoutStepTwo")
    @allure.severity(allure.severity_level.MINOR)
    def test_remove_item_from_checkout_step2(self, logged_in_browser, base_url):

        with allure.step("Inject items to LocalStorage"):
            logged_in_browser.execute_script("window.localStorage.setItem('cart-contents', '[0,1,5]')") 
            logged_in_browser.get(f"{base_url}checkout-step-one.html")

        checkstep1_page = CheckoutStepOnePage(logged_in_browser)
        checkstep1_page.fill_form("John", "Doe", "1751784")
        checkstep1_page.click_continue()

        checkstep2_page = CheckoutStepTwoPage(logged_in_browser)
        all_items = checkstep2_page.get_items_names()
        target_item_name = random.choice(all_items)
        checkstep2_page.open_item_card(target_item_name)
        all_items.remove(target_item_name)

        item_card_page = ItemCardPage(logged_in_browser)
        item_card_page.remove_from_cart()
        item_card_page.go_to_inventory()

        inventory_page = InventoryPage(logged_in_browser)

        with allure.step("Checking that cart badge is now 2"):
            assert inventory_page.get_text_from_cart_badge() == "2"
        inventory_page.open_cart()

        cart_page = CartPage(logged_in_browser)
        cart_items = cart_page.get_all_names_in_cart()
        
        with allure.step("Checking that cart-contents are valid"):
            assert sorted(cart_items) == sorted(all_items), f"Expected items {all_items}, but in cart {cart_items}"