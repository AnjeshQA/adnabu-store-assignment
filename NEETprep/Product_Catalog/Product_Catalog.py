import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
from NEETprep.NEETprep_Login import driver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)


class Product_Catalog():
    def buy_new_courses(self):
        driver.get("https://dev.neetprep.com/newui/OffersDisplay")
        time.sleep(10)

        driver.find_element(By,)
