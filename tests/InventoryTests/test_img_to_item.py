import allure

from pages.inventory_page import InventoryPage
from constants.constants import EXPECTED_IMAGES_MAP

@allure.feature("Inventory Test")
class TestInventory:

    @allure.title("Check if image matches item")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_img_to_item(self, logged_in_browser):
        inventory_page = InventoryPage(logged_in_browser)

        item_names = inventory_page.get_all_names_items()

        for item_name in item_names:
            src = inventory_page.get_src_of_img(item_name)
            expected_keyword = EXPECTED_IMAGES_MAP.get(item_name)

            assert src is not None, f"Item '{item_name} does not have src tag"

            assert expected_keyword is not None, f"Item '{item_name}' isnt in map EXPECTED_IMAGES_MAP"

            with allure.step(f"Checking image mapping for {item_name}"):
                assert expected_keyword in src, f"Found wrong image on item '{item_name}'! src: '{src}'"
