import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilities import readconfig


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="class")
def driver_setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options)
    else:
        print("Invalid browser")

    driver.get(readconfig.ReadConfig.get_login_url())
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()