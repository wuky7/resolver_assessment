import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_6(browser):
    logging.info('Running test case 6')

    # method that allows you to find the value of any cell on the grid
    def get_cell_value(row, column):

        # Wait for the table to be displayed
        table = browser.find_element(By.XPATH, '//*[@id="test-6-div"]/div/table/tbody')

        # Find the row and column elements
        row_element = table.find_elements(By.TAG_NAME, 'tr')[row]
        column_element = row_element.find_elements(By.TAG_NAME, 'td')[column]

        # Get the cell value
        cell_value = column_element.text

        return cell_value

    # Get the value of the cell at coordinates 2, 2
    cell_value = get_cell_value(2, 2)

    # Assert that the cell value is "Ventosanzap"
    assert cell_value == "Ventosanzap", f"Cell value is {cell_value}, expected 'Ventosanzap'"
