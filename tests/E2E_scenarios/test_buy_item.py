import pytest
import random
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


@allure.feature("E2E : buy item scenario")
@allure.title("Full happy path of making an order to buy an item")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_item(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)

    item_names = inventory_page.get_all_names_items()
    item_prices = inventory_page.get_all_prices()
    all_items = list(zip(item_names, item_prices))

    expected_items = random.sample(all_items, 3)
    for item_name, item_price in expected_items:
        locator = inventory_page._item_name_to_locator(item_name)
        inventory_page.add_item_to_cart_dynamic(locator)

    inventory_page.open_cart()

    cart_page = CartPage(logged_in_browser)

    cart_names = cart_page.get_all_names_in_cart()
    cart_prices = cart_page.get_all_prices_in_cart()
    cart_items = list(zip(cart_names, cart_prices))

    with allure.step("Checking if the items chosen in inventory and the items in cart are the same"):
        assert sorted(cart_items) == sorted(expected_items)
    cart_page.click_checkout_button()

    checkout_step_one_page = CheckoutStepOnePage(logged_in_browser)
    checkout_step_one_page.fill_form("FirstName", "LastName", "01722489")
    checkout_step_one_page.click_continue()

    checkout_step_two_page = CheckoutStepTwoPage(logged_in_browser)
    check2_items_names = checkout_step_two_page.get_items_names()
    check2_items_prices = checkout_step_two_page.get_items_prices()
    check2_items = list(zip(check2_items_names, check2_items_prices))
    with allure.step("Checking if the items in cart and the items in checkoutStep2 page are the same"):
        assert sorted(cart_items) == sorted(check2_items)
    
    total_cost_items_from_label = checkout_step_two_page.get_total_item_cost()
    sum_cost_of_items = checkout_step_two_page.sum_of_items_prices()

    with allure.step("Checking if the total cost label displays actual cost of all items"):
        assert total_cost_items_from_label == sum_cost_of_items

    tax_from_label = checkout_step_two_page.get_tax_label()
    calculated_tax = sum_cost_of_items * 0.08

    with allure.step("Checking if the tax calculations are right"):
        assert tax_from_label == round(calculated_tax, 2)

    total_with_tax_from_label = checkout_step_two_page.get_total_label()
    calculated_total_with_tax = sum_cost_of_items + calculated_tax

    with allure.step("Checking if total cost calculations are right"):
        assert total_with_tax_from_label == round(calculated_total_with_tax, 2)
    checkout_step_two_page.click_finish_button()

    checkout_complete_page = CheckoutCompletePage(logged_in_browser)
    complete_header_text = checkout_complete_page.get_text_from_complete_header()

    with allure.step("Checking if the order is completed"):
        assert complete_header_text == "Thank you for your order!"