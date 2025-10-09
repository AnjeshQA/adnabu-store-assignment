import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Import the Service class

@pytest.fixture()

def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Example: you can add other options as needed.

    # Create a Service object for ChromeDriver
    service = Service(ChromeDriverManager().install())  # Use ChromeDriverManager to install the correct driver

    # Initialize the Chrome WebDriver with the Service object and options
    request.cls.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the website
    request.cls.driver.get("https://www.neetprep.com/login")

    # Wait for elements to load (implicitly)
    request.cls.driver.implicitly_wait(10)

    yield
    request.cls.driver.quit()