from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD
from utils.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE

def test_checkout_flow(page):
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    checkout = CheckoutPage(page)
    checkout.complete_checkout(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    assert "Thank you for your order!" in checkout.get_success_message()