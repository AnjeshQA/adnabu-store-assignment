import pytest
from NEETprep.PageObject.LoginPage import Login
from selenium.webdriver.common.by import By
from NEETprep.TestCase.configTest import setup
@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_LT_001(self):
        lg = Login(self.driver)
        # Perform login steps
        #self.driver.find_element(By.XPATH, "//input[@id='number']").send_keys("9000000000")
        lg.enter_mobile_no("9000000000")

        #self.driver.find_element(By.XPATH, "//button[@id='otp_button']").click()
        lg.send_otp()

        #self.driver.find_element(By.XPATH, "//input[@id='code']").send_keys("876302")
        lg.enter_otp("876302")

        #self.driver.find_element(By.XPATH, "//button[@id='otp_button']").click()
        lg.verify_otp()

        #if 'Practice Session' in self.driver.find_element(By.XPATH,"//div[normalize-space()='Practice Session']").text:
        if 'Practice Session' in lg.homepage():
            assert True
        else:
            assert False

    def test_LT_002(self):
        lg = Login(self.driver)
        # Perform login steps
        #self.driver.find_element(By.XPATH, "//input[@id='number']").send_keys("9000000000")
        lg.enter_mobile_no("9000000000")

        #self.driver.find_element(By.XPATH, "//button[@id='otp_button']").click()
        lg.send_otp()

        #self.driver.find_element(By.XPATH, "//input[@id='code']").send_keys("876303")
        lg.enter_otp("876303")

        #self.driver.find_element(By.XPATH, "//button[@id='otp_button']").click()
        lg.verify_otp()

        if 'Invalid OTP. Please try again.' in lg.invalid_otp_error_msz():
            assert True
        else:
            assert False

# Optional: Close the driver at the end
# driver.quit()
