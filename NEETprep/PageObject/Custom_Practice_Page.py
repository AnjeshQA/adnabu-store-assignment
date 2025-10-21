from selenium.webdriver.common.by import By

class CustomTest:
    def __init__(self, driver):
        self.driver = driver

        self.click_custom_practice_session_Xpath = "//div[normalize-space()='Custom Practice Session']"
        self.close_unfinish_test_popup_xpath = "//div[@class='block absolute top-2 right-2 cursor-pointer']//*[name()='svg']"
        self.start_fresh_test_Xpath = "//button[contains(text(), 'No, Start Fresh')]"
        self.resume_test_button_Xpath = "//button[contains(text(), 'Resume Test')]"
        self.view_all_test_attempt_Xpath = "//button[normalize-space()='View Test Attempts']"
        self.search_chapters_ct_Xpath = "//input[@id='input-search']"
        self.select_a_chapter_Xpath = "//input[@id='c675']"
        self.continue_button_ct_Xpath = "//button[text()='Continue']"
        self.print_pdf_ct_Xpath = "//button[text()='Print PDF']"
        self.pdf_generated_Xpath = "//div[normalize-space()='Fill OMR Sheet*']"

    def click_custom_test_button(self):
        self.driver.find_element(By.XPATH, self.click_custom_practice_session_Xpath).click()

    def close_resume_test_popup(self):
        self.driver.find_element(By.XPATH, self.close_unfinish_test_popup_xpath).click()

    def select_chapter(self):
        self.driver.find_element(By.XPATH, self.select_a_chapter_Xpath).click()

    def continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_ct_Xpath).click()

    def print_pdf(self):
        self.driver.find_element(By.XPATH, self.print_pdf_ct_Xpath).click()

    def pdf_generate(self):
        return self.driver.find_element(By.XPATH, self.pdf_generated_Xpath).text

    #or pdf text alternative

    # def pdf_generate(self):
    #     element = self.driver.find_element(By.XPATH, self.pdf_generated_Xpath)
    #     return element.text


