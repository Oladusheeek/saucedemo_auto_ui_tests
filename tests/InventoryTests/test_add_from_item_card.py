from pages.inventory_page import InventoryPage
from pages.item_card_page import ItemCardPage

import random

def test_add_from_item_cart(logged_in_browser):
    inventory_page = InventoryPage(logged_in_browser)

    items = inventory_page.get_all_items()

    item = random.choice(items)
    name_inventory = item[0]
    price_inventory = item[1]
    inventory_page.click_item_title(name_inventory)

    assert "inventory-item" in logged_in_browser.current_url

    item_card_page = ItemCardPage(logged_in_browser)
    name_card = item_card_page.get_name()
    price_card = item_card_page.get_price()

    assert name_inventory == name_card
    assert price_inventory == price_card

    item_card_page.add_to_cart()

    assert item_card_page.get_text_from_cart_badge() == "1"
    assert item_card_page.get_text_remove_button() == "Remove"