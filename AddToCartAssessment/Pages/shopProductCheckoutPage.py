from Pages.BasePage import BasePage
from Utilities import configReader

class shopProductCheckout(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_password(self, password):
        self.type("passwordTextBox_ID", password)

    def submit_password(self):
        self.click("submitPasswordButton_XPATH")

    def search_product(self, product_name):
        self.click("clickSearchIcon_CSS")
        # Ensure your BasePage type method takes (locator_key, value)
        self.type("inputSearchBox_XPATH", product_name)

    def select_product(self):  # Removed unused product_name argument
        # Fix: Key must match .ini (productName)
        product_name = configReader.readConfig("common info", "productName")

        raw_xpath = configReader.readConfig("locators", "TheCompleteSnowboard_XPATH")

        # Format the XPATH: //p[normalize-space()='The Videographer Snowboard']
        final_xpath = raw_xpath.format(product_name)

        # Use the manual click helper
        self.click_element_manual(final_xpath)

    def click_add_to_cart(self):
        self.click("addToCartButton_XPATH")

    def verify_checkout_page(self):
        self.click("checkout_XPATH")
        # We scroll first to ensure the button is in the DOM/View
        self.scroll_into_view("payNowButton_XPATH")
        # Now we check if it's actually there
        assert self.is_element_displayed("payNowButton_XPATH"), "Checkout failed: Pay Now button not visible!"

