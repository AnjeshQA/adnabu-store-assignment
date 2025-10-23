from time import sleep
import pytest
from NEETprep.PageObject.Custom_Practice_Page import CustomTest
from NEETprep.PageObject.Login_Page import Login
from selenium.webdriver.common.by import By
from NEETprep.TestCase.configTest import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestCustom:

    def test_CT_001(self):
        # Set implicit wait for the driver (e.g., 10 seconds)
        self.driver.implicitly_wait(30)

        lg = Login(self.driver)
        ct = CustomTest(self.driver)

        # Login steps
        lg.enter_mobile_no("9000000000")
        lg.send_otp()
        lg.enter_otp("876302")
        lg.verify_otp()
        #lg.checkin()

        # Custom test steps
        sleep(5)
        ct.click_custom_test_button()
        ct.close_resume_test_popup()
        ct.select_chapter()
        ct.continue_button()
        sleep(2)
        ct.continue_button()
        ct.print_pdf()

        # Verification
        if "Fill OMR Sheet*" in ct.pdf_generate():
            assert True
        else:
            assert False

    def test_CT_002(self):
        self.driver.implicitly_wait(30)

        lg = Login(self.driver)
        ct = CustomTest(self.driver)

        # Login steps
        lg.enter_mobile_no("9000000000")
        lg.send_otp()
        lg.enter_otp("876302")
        lg.verify_otp()
        #lg.checkin()

        # Custom test steps
        sleep(5)
        ct.click_custom_test_button()
        ct.close_resume_test_popup()
        ct.select_chapter()
        sleep(3)
        ct.continue_button()
        sleep(3)
        ct.continue_button()
        sleep(3)
        ct.start_test()
        sleep(3)
        # Loop to select option and go next 5 times
        for _ in range(5):
            ct.select_option()  # Select option for the current question
            ct.go_next()  # Click "Next" to go to the next question

        ct.submit_test()
        ct.continue_button()
        ct.go_to_analytics()
        ct.go_home()

        if 'Practice Session' in lg.homepage():
            assert True
        else:
            assert False


