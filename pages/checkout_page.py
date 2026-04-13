from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"
    FINISH_BTN = "#finish"
    SUCCESS_MSG = ".complete-header"

    def complete_checkout(self, first, last, zip_code):
        self.click(self.CHECKOUT_BTN)
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)
        self.click(self.FINISH_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)