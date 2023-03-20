import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_5(browser):
    logging.info('Running test case 5')

    # In the test 5 div, wait for a button to be displayed (note: the delay is random) and then click it
    display_button = browser.find_element(By.ID, 'test5-button')

    # Wait until the element is displayed
    while not display_button.is_displayed():
        pass
    logging.info('Button is now displayed')
    display_button.click()
    logging.info('Button is now clicked')
    # Adding sleep to see script in action
    time.sleep(5)

    # assert that a success message is displayed

    success_message = browser.find_element(By.ID, 'test5-alert').text
    #Adding sleep to see script in action
    time.sleep(10)
    # Assert that the alert text contains "You clicked a button!"
    assert "You clicked a button!" in success_message
    logging.info('You clicked a button! success message asserted')


    # Assert that the button is now disabled

    assert display_button.get_attribute("disabled") == "true", 'The button is not disabled'
    logging.info('The button is disabled')
