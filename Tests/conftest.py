import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from selenium import webdriver
from PageObjects.homePage import HomePage
import pytest
import platform
platform = platform.system()


@pytest.fixture()
def driver():
<<<<<<< HEAD

	driver_path = os.path.join(myPath, "../TestResources/drivers/chromedriver")
=======
    driver_path = os.path.join(myPath, "../TestResources/drivers/chromedriver")
    if(platform!='Windows'):
        driver_path = driver_path.replace("/Tests/TestResources/drivers/chromedriver","/TestResources/drivers/chromedriver")
>>>>>>> 41fa014271ffd882b2d7cb0fbd42a3d4f28f6285
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.set_window_size(1260, 1080)
    return driver

@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver)
    return home_page



