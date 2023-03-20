import logging

import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_1(browser):
    logging.info('Running test case 1')

    # Find elements & Assert that all three elements are present on the page

    email_input = browser.find_element(By.ID, "inputEmail")
    assert email_input.is_displayed()
    password_input = browser.find_element(By.ID, "inputPassword")
    assert password_input.is_displayed()
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert login_button.is_displayed()
    logging.info('email, password and signin button present')

    # Enter in an email address and password combination into the respective fields
    email_input.send_keys('parth@resolver.ca')
    password_input.send_keys('password')




