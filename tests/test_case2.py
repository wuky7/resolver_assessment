import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_2(browser):
    logging.info('Running test case 2')

    # In the test 2 div, assert that there are three values in the listgroup
    listgroup = browser.find_elements(By.CLASS_NAME, "list-group-item")
    list_items = len(listgroup)
    assert list_items == 3

    # Assert that the second list item's value is set to "List Item 2"
    # Here, I tried getting the element using NOT span value to not include the badge value returned but was unsuccessful, hence used the string split method
    second_list_item = " ".join(listgroup[1].text.split()[0:3])
    assert second_list_item == "List Item 2"

    # Assert that the second list item's badge value is 6
    second_item_badge_value = browser.find_element(By.XPATH, '//*[@id="test-2-div"]/ul/li[2]/span')
    assert second_item_badge_value.text == "6"


