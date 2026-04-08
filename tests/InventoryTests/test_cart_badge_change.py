import pytest

from utility_funcs.load_data import load_data_json
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("test_data", load_data_json("add_to_cart_data.json"))
def test_add_to_cart(logged_in_browser, test_data):
    actual_item_name = test_data["item_name"]
    inventoryPage = InventoryPage(logged_in_browser)
    inventoryPage.add_item_to_cart_dynamic(actual_item_name)
    inventoryPage.wait_for_cart_badge_to_update("1")
    
    assert inventoryPage.get_text_from_cart_badge() == "1"