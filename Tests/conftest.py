import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from selenium import webdriver
from PageObjects.homePage import HomePage
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    #driver_path = os.path.join(myPath, "TestResources/drivers/chromedriver")
    #driver_path = driver_path.replace("/Tests/TestResources/drivers/chromedriver","/TestResources/drivers/chromedriver.exe")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.set_window_size(1260, 1080)
    return driver

@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver)
    return home_page



