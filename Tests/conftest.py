import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
print(myPath)
sys.path.insert(0, myPath + '/../')
from selenium import webdriver
from PageObjects.homePage import HomePage
import pytest
from selenium.webdriver.chrome.options import Options
import platform 
platform = platform.system()


@pytest.fixture()
def driver():
    if platform == 'Windows':
        driver_path = os.path.join(myPath, "../TestResources/drivers/chromedriver")
        driver = webdriver.Chrome(driver_path)
    
    elif platform == 'Linux':
     
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/bin/chromedriver/chromedriver',chrome_options=chrome_options)
        
    return driver

@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver)
    return home_page
