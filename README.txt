Summary

The solution for the take home assessment from Resolver has been implemented by using selenium webdriver and python. The framework used is pytest.
The test scripts are all under the folder path resolver_assessment/tests. The tests are designed to run on chrome browser.


Setup

In order to run the scripts, we need the following:
1. chrome driver : https://chromedriver.chromium.org/downloads
2. selenium : https://selenium-python.readthedocs.io/index.html   [pip install -U selenium]
3. pytest : https://pypi.org/project/pytest/   [pip install pytest]


Run tests

1. First, change the baseURL path in the tests/conftest.py file
2. In the project directory within terminal, run command pytest