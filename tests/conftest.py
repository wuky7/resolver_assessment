from selenium import webdriver
import pytest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="session")
def browser():
    # Create an instance of the Chrome browser
    driver = webdriver.Chrome()

    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the base URL
    baseURL = "file:///Users/parthshah/Downloads/QE-index.html"
    driver.get(baseURL)

    # Add an implicit wait of 2000 milliseconds
    driver.implicitly_wait(2000)


    # Return the driver object to the test function
    yield driver

    # Close the browser window after the test is completed
    driver.quit()
