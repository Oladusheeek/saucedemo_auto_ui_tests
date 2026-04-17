import random
from pages.inventory_page import InventoryPage

def test_reset_app_state(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)

    all_items = inventory_page.get_all_items()
    expected_items = random.sample(all_items, 3)
    for item_name, item_price in expected_items:
        locator = inventory_page._item_name_to_locator(item_name)
        inventory_page.add_item_to_cart_dynamic(locator)

    assert inventory_page.get_text_from_cart_badge() == "3"

    inventory_page.click_burger_menu_button()
    inventory_page.reset_app_state()

    assert inventory_page.is_cart_badge_present() == False

def test_logout(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)

    inventory_page.click_burger_menu_button()
    inventory_page.logout()

    assert logged_in_browser.current_url == "https://www.saucedemo.com/"

    
