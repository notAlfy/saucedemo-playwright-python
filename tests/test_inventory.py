from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import USERNAME, PASSWORD

def test_add_to_cart(page):
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert "cart" in page.url