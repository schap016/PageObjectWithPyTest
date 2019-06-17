import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from selenium import webdriver
from PageObjects.homePage import HomePage
import pytest


@pytest.fixture()
def driver():
    driver_path = os.path.join(myPath, "../TestResources/drivers/chromedriver")
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(5)
    driver.set_window_size(1260, 1080)
    return driver

@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver)
    return home_page



