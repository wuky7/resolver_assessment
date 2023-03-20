import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_3(browser):
    logging.info('Running test case 3')

    # In the test 3 div, assert that "Option 1" is the default selected value
    default_selected = browser.find_element(By.ID, "dropdownMenuButton")
    time.sleep(5)
    assert default_selected.text == "Option 1"

    # Select "Option 3" from the select list
    default_selected.click()
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="test-3-div"]/div/div/a[3]').click()
    time.sleep(5)