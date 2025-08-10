import time
import datetime
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Setup WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 1: Open the website
driver.get("https://erail.in/")

# Step 2-3: Clear the "From" field
from_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='txtStationFrom']"))
)
from_field.click()
from_field.clear()
time.sleep(1)

# Step 4: Insert "DEL" in the field to open the dropdown
from_field.send_keys("DEL")
time.sleep(2)  # Wait for dropdown to appear

# Step 5: Select the 4th position station in the dropdown & print it

dropdown_items = driver.find_elements(By.XPATH, "//div[@title='Delhi Azadpur']//div[1]")

# if len(dropdown_items) >= 4:
#     station_name = dropdown_items[3].text  # Get 4th station text
#     print(f"Selected Station: {station_name}")
#     dropdown_items[3].click()
# else:
#     print("Less than 4 options available in the dropdown!")

# Step 6: Create an Excel file with expected station names
# expected_stations = ["NEW DELHI", "DELHI", "DELHI CANTT", "HAZRAT NIZAMUDDIN"]
time.sleep(200)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Expected Stations"
ws.append(["Expected Station Names"])
for station in expected_stations:
    ws.append([station])
wb.save("expected_stations.xlsx")

# Step 7: Get the list of actual drop-down values & write them into an Excel file
actual_stations = [item.text for item in dropdown_items]

wb_actual = openpyxl.Workbook()
ws_actual = wb_actual.active
ws_actual.title = "Actual Stations"
ws_actual.append(["Actual Station Names"])
for station in actual_stations:
    ws_actual.append([station])
wb_actual.save("actual_stations.xlsx")

# Step 7.1: Compare expected vs actual stations
expected_set = set(expected_stations)
actual_set = set(actual_stations)
matched_stations = expected_set.intersection(actual_set)
print(f"Matched Stations: {matched_stations}")

# Step 8: Select 30 days from today in "Sort on Date"
today = datetime.date.today()
future_date = today + datetime.timedelta(days=30)
formatted_date = future_date.strftime("%d-%m-%Y")

date_picker = driver.find_element(By.XPATH, "//input[@id='txtJourneyDate']")
date_picker.click()
date_picker.clear()
date_picker.send_keys(formatted_date)  # Insert dynamically calculated date
date_picker.send_keys(Keys.RETURN)  # Press Enter to confirm

print(f"Selected Date: {formatted_date}")

# Step 9: Generate Extent Report
import pytest
from pytest_html import extras

@pytest.mark.parametrize("selected_station", matched_stations)
def test_selected_station(selected_station):
    assert selected_station in expected_stations, f"Station {selected_station} not expected!"

@pytest.mark.parametrize("selected_date", [formatted_date])
def test_selected_date(selected_date):
    assert selected_date == formatted_date, "Date mismatch!"

# Run pytest to generate the report
pytest.main(["--html=extent_report.html", "--self-contained-html"])

# Close the browser
time.sleep(3)
driver.quit()
