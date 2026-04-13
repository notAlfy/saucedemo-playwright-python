from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = ".inventory_item button"
    CART_ICON = ".shopping_cart_link"

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def go_to_cart(self):
        self.click(self.CART_ICON)