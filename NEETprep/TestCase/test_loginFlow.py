import pytest
from NEETprep.PageObject.Login_Page import Login
from selenium.webdriver.common.by import By
from NEETprep.TestCase.configTest import setup
@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_LT_001(self):
        lg = Login(self.driver)
        lg.enter_mobile_no("9000000000")
        lg.send_otp()
        lg.enter_otp("876302")
        lg.verify_otp()
        if 'Practice Session' in lg.homepage():
            assert True
        else:
            assert False

    def test_LT_002(self):
        lg = Login(self.driver)
        # Perform login steps
        lg.enter_mobile_no("9000000000")
        lg.send_otp()
        lg.enter_otp("876303")
        lg.verify_otp()
        if 'Invalid OTP. Please try again.' in lg.invalid_otp_error_msz():
            assert True
        else:
            assert False
