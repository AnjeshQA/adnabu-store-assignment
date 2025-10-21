from time import sleep

import pytest
from NEETprep.PageObject.Custom_Practice_Page import CustomTest
from NEETprep.PageObject.Login_Page import Login
from selenium.webdriver.common.by import By
from NEETprep.TestCase.configTest import setup

@pytest.mark.usefixtures("setup")
class TestCustom:

    def test_CT_001(self):
        # Set implicit wait for the driver (e.g., 10 seconds)
        self.driver.implicitly_wait(20)

        lg = Login(self.driver)
        ct = CustomTest(self.driver)

        # Login steps
        lg.enter_mobile_no("9000000000")
        lg.send_otp()
        lg.enter_otp("876302")
        lg.verify_otp()
        #lg.checkin()

        sleep(5)
        # Custom test steps
        ct.click_custom_test_button()
        sleep(2)
        ct.close_resume_test_popup()
        sleep(2)
        ct.select_chapter()
        sleep(2)
        ct.continue_button()
        sleep(2)
        ct.continue_button()
        sleep(2)
        ct.print_pdf()
        sleep(3)

        # Verification
        if "Fill OMR Sheet*" in ct.pdf_generate():
            assert True
        else:
            assert False

