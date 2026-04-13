from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)

    assert "inventory" in page.url