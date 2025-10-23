
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.pdf_generated_assert_Xpath = "//div[normalize-space()='Fill OMR Sheet*']"
        self.start_test_button_Xpath = "//button[@class='w-full transition-colors text-white py-3.5 px-5 rounded-[10px] text-base font-semibold cursor-pointer bg-primary hover:bg-primary-dark']"
        self.select_correct_options_Xpath = "//button[@id='option-2']"
        self.go_to_next_question_Xpath = "(//*[name()='path'])[13]"
        self.submit_test_Xpath = "(//button[normalize-space()='Yes'])[1]"
        self.go_to_test_analytics_page_Xpath = "//button[text()='Continue your journey']"
        self.go_to_home_page_Xpath = "//button[text()='Go Home']"

    # def click_custom_test_button(self):
    #     self.driver.find_element(By.XPATH, self.click_custom_practice_session_Xpath).click()

    def click_custom_test_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.click_custom_practice_session_Xpath))
        ).click()

    def close_resume_test_popup(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_unfinish_test_popup_xpath))
        ).click()

    def select_chapter(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_a_chapter_Xpath))
        ).click()

    def continue_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button_ct_Xpath))
        ).click()

    def print_pdf(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.print_pdf_ct_Xpath))
        ).click()
    # assertion to check pdf generated or not
    def pdf_generate(self):
        # Ensure we wait for the element to be clickable and then get its text
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pdf_generated_assert_Xpath))
        )
        return element.text  # Return the text of the element

    #or pdf text alternative

    # def pdf_generate(self):
    #     element = self.driver.find_element(By.XPATH, self.pdf_generated_Xpath)
    #     return element.text

    def start_test(self):
        WebDriverWait(self.driver,30).until(
            EC.element_to_be_clickable((By.XPATH,self.start_test_button_Xpath))
        ).click()

    def select_option(self):
        WebDriverWait(self.driver,30).until(
            EC.element_to_be_clickable((By.XPATH,self.select_correct_options_Xpath))
        ).click()

    def go_next(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_to_next_question_Xpath))
        ).click()

    def submit_test(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_test_Xpath))
        ).click()

    def go_to_analytics(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_to_test_analytics_page_Xpath))
        ).click()

    def go_home(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_to_home_page_Xpath))
        ).click()




