from pytest_bdd import scenarios, given, when, then
from Pages.shopProductCheckoutPage import shopProductCheckout
from Utilities import configReader

scenarios('../features/shopProductCheckout.feature')


@given('User successfully logged in to the Adnabu store')
def login_bypass(driver):
    # Fetch credentials from [common info]
    url = configReader.readConfig("common info", "url")
    pw = configReader.readConfig("common info", "PW")

    driver.get(url)
    shop = shopProductCheckout(driver)
    shop.enter_password(pw)
    shop.submit_password()


@given('I am on the store homepage')
def verify_home(driver):
    expected_partial_url = configReader.readConfig("common info", "url_shop")
    # Verify we are no longer on the /password page
    assert expected_partial_url in driver.current_url


@when('I search for the configured product')
def search_product(driver):
    product = configReader.readConfig("common info", "productName")
    shop = shopProductCheckout(driver)
    shop.search_product(product)


@when('I add the product to my cart')
def add_to_cart(driver):
    shop = shopProductCheckout(driver)
    # This method handles the dynamic XPATH with {0}
    shop.select_product()
    shop.click_add_to_cart()


@then('I should see the product in the checkout summary')
def verify_checkout(driver):
    shop = shopProductCheckout(driver)
    shop.verify_checkout_page()