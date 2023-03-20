import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_4(browser):
    logging.info('Running test case 4')

    # assert that the first button is enabled
    first_button = browser.find_element(By.XPATH, '//*[@id="test-4-div"]/button[1]')
    assert first_button.is_enabled()

    #assert second button is disabled
    second_button = browser.find_element(By.XPATH, '//*[@id="test-4-div"]/button[2]')
    assert second_button.get_attribute("disabled") == "true"

    #adding time sleep to see script in action
    time.sleep(5)