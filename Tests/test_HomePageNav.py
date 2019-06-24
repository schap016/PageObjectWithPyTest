import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import pytest


baseUrl = "https://www.phptravels.net/"


@pytest.mark.dependency()
def test_home_page_navigation_to_PHPTravels(driver,home_page,screenshot_path):
    driver.get(baseUrl)
    home_page_nav = home_page.is_title_matches()
    if home_page_nav:
       assert True
       driver.close()
    else:
       driver.save_screenshot(screenshot_path + "test_home_page_navigation_to_PHPTravels.png")
       driver.close()
       assert False



@pytest.mark.dependency(depends=["test_home_page_navigation_to_PHPTravels"])
def test_verify_booking_tabs(driver,home_page,screenshot_path):
    driver.get(baseUrl)
    _primary_tabs_verified = home_page.verify_primary_tabs_homePage()
    if _primary_tabs_verified:
        driver.close()
        assert True
    else:

        driver.save_screenshot(screenshot_path + "test_verify_booking_tabs.png")
        driver.close()
        assert False














