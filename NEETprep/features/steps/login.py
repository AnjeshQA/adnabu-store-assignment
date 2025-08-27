from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_OTP_from_file():
    try:
        file_path = "/Users/ssd/Desktop/PW.txt"  # Use plain text file
        with open(file_path, "r") as file:
            otp = file.read().strip()  # Strip any whitespace
            print(f"OTP read from file: '{otp}'")  # Debugging
        return otp
    except FileNotFoundError:
        raise Exception(f"Password file not found at {file_path}. Please ensure it exists.")
    except Exception as e:
        raise Exception(f"Error reading password file: {e}")

@given(u'I am on the NEETprep login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.neetprep.com/login")
    print("Inside - NEETprep login page")


@when(u'I enter my mobile number')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@id='number']").send_keys("9000000000")
    print("Inside - entered mobile number")


@when(u'I click the Send OTP button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@id='otp_button']").click()
    print("Inside - clicked Send OTP button")


@when(u'I enter the OTP')
def step_impl(context):
    # Fetch OTP from the file
    otp = get_OTP_from_file()
    #context.driver.find_element(By.XPATH,"//input[@id='code']")
    # Wait for the OTP field to appear and enter the OTP
    print("Waiting for the OTP field...")
    otp_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "code"))
    )
    print(f"Entering OTP: '{otp}'")  # Debugging
    otp_field.send_keys(otp)

    time.sleep(3)
    print("Inside - entered OTP")


@when(u'I click the Verify OTP button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//span[@id='buttonText']").click()
    print("Inside - clicked Verify OTP button")


@then(u'I should see the NEETprep home page')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Home").is_displayed()

    # expected_url = "https://www.neetprep.com/home"
    #
    # # Wait for URL
    # WebDriverWait(context.driver, 10).until(
    #     lambda driver: driver.current_url == expected_url
    # )
    #
    # # Wait for a unique element (example: logout button)
    # WebDriverWait(context.driver, 10).until(
    #     EC.visibility_of_element_located((By.ID, "logoutBtn"))
    # )
    print("Inside - NEETprep home page displayed")

    time.sleep(200)



@when(u'I enter the ivalid OTP')
def step_impl(context):
    print("Inside - entered invalid OTP")


@then(u'Proper Error Message should be displayed due to invalid OTP')
def step_impl(context):
    print("Inside - Proper Error Message displayed due to invalid OTP")


@given(u'I am on the NEETprrp Login page')
def step_impl(context):
    print("Inside - NEETprrp Login page")


@when(u'I click the Send OTP buttion')
def step_impl(context):
    print("Inside - clicked Send OTP button (typo version)")


@when(u'I didnt enter any OTP')
def step_impl(context):
    print("Inside - did not enter any OTP")


@when(u'I click the verify OTP button')
def step_impl(context):
    print("Inside - clicked verify OTP button")


@then(u'Proper Error Validation message Please enter the OTP should be displayed')
def step_impl(context):
    print("Inside - Error Message: Please enter the OTP")


@when(u'I enter a valid mobile number')
def step_impl(context):
    print("Inside - entered valid mobile number")


@when(u'I enter any expired OTP')
def step_impl(context):
    print("Inside - entered expired OTP")


@then(u'Proper Error Validation message for expired OTP should be displayed')
def step_impl(context):
    print("Inside - Error Message for expired OTP")


@when(u'I didnt enter any mobile number')
def step_impl(context):
    print("Inside - did not enter any mobile number")


@when(u'I enter a valid OTP')
def step_impl(context):
    print("Inside - entered valid OTP")