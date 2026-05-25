import allure

from pages.inventory_page import InventoryPage

@allure.feature("Test Mocking")
class TestMocking:

    @allure.title("Mocking 'Image not found' error")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mock_broken_images(self, logged_in_browser):
        browser = logged_in_browser

        def block_images(request):
            if '.jpg' in request.url:
                request.create_response(
                    status_code=404,
                    headers = {'Content-Type': 'text/html'},
                    body = b'Image Not Found Mock'
                )
        with allure.step("Enabling interceptor"):
            browser.request_interceptor = block_images

        try:
            with allure.step("Refreshing page to enable mock"):
                browser.refresh()
                inventory_page = InventoryPage(logged_in_browser)
            
            images = inventory_page.get_all_item_images()

            with allure.step("Checking if images are broken"):
                for img in images:
                    is_image_broken = browser.execute_script("return arguments[0].naturalWidth === 0;", img)
                    assert is_image_broken, "Error: image was loaded. Mock wasn't triggered"
        finally:
            with allure.step("Deleting interceptor"):
                del browser.request_interceptor