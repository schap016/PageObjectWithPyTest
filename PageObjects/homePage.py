from selenium.webdriver.common.by import By
from SupportClasses.pageobject_support import callable_find_by as find_by
from selenium.common.exceptions import NoSuchElementException

class HomePage():
    """Home page action methods come here"""
    def __init__(self, driver):
        self.driver = driver
        self.HOTELS_TAB = find_by(how=By.XPATH,using ="//*[contains(@href,'#hotels')]")
        self.FLIGHTS_TAB = find_by(how=By.XPATH,using ="//*[contains(@href,'#flights')]")
        self.TOURS_TAB = find_by(how=By.XPATH, using="//*[contains(@href,'#tours')]")
        self.CARS_TAB = find_by(how=By.XPATH, using="//*[contains(@href,'#cars')]")

    #"""Verifies page title of home page for PHP Travels"""
    def is_title_matches(self):
        if self.driver.title == "PHPTRAVELS | Travel Technology Partner":
            return True
        return False

    #"""Verifies primary tabs on home page"""
    def verify_primary_tabs_homePage(self):
        try:
            self.HOTELS_TAB
            self.FLIGHTS_TAB
            self.TOURS_TAB
            self.CARS_TAB
        except NoSuchElementException:
            return False
        return True


