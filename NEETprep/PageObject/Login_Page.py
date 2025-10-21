from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):  # Change __int__ to __init__
        self.driver = driver
        self.enter_mobile_no_Xpath = "//input[@id='number']"
        self.sent_otp_button_Xpath = "//button[@id='otp_button']"
        self.enter_mobile_otp_Xpath = "//input[@id='code']"
        self.verify_otp_button_Xpath = "//button[@id='otp_button']"
        self.invalid_otp_error_message_Xpath = "//div[@class='alert api-alert text-center font-weight-bold alert-danger']"
        self.homepage_Xpath = "//div[normalize-space()='Practice Session']"
        self.check_in_counter_Xpath = "//a[@class='wzrkClose']"



    def enter_mobile_no(self, mobileNo):
        self.driver.find_element(By.XPATH, self.enter_mobile_no_Xpath).send_keys(mobileNo)

    def send_otp(self):
        self.driver.find_element(By.XPATH, self.sent_otp_button_Xpath).click()

    def enter_otp(self, otp):
        self.driver.find_element(By.XPATH, self.enter_mobile_otp_Xpath).send_keys(otp)

    def verify_otp(self):
        self.driver.find_element(By.XPATH, self.verify_otp_button_Xpath).click()

    def invalid_otp_error_msz(self):
        return self.driver.find_element(By.XPATH, self.invalid_otp_error_message_Xpath).text

    def homepage(self):
        return self.driver.find_element(By.XPATH,self.homepage_Xpath).text

    def checkin(self):
        self.driver.find_element(By.XPATH, self.check_in_counter_Xpath).click()
