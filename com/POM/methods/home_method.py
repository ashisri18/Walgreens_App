from selenium.webdriver.common.action_chains import ActionChains
from com.POM.locators.home_loc import *
from selenium.webdriver.common.keys import Keys
import time
from com.generic_lib.listener import *
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):

    def navigate_Prescription_Health_Screen(self):
        element = self.driver.find_element(*HomeLoc.PRESCRIPTIONS_BTN)
        element.click()
        time.sleep(2)

    def navigate_Shop_Products_Screen(self):
        element = self.driver.find_element(*HomeLoc.SHOP_BTN)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)

    def navigate_Photo_Screen(self):
        element = self.driver.find_element(*HomeLoc.PHOTO_BTN)
        element.click()
        time.sleep(2)

    def navigate_Weekly_Ad_Screen(self):
        element = self.driver.find_element(*HomeLoc.WEEKLY_ADS_TXT)
        element.click()

    def navigate_Refill_Screen(self):
        element = self.driver.find_element(*HomeLoc.REFILL_ICN)
        element.click()

    def navigate_Rewards_Screen(self):
        element = self.driver.find_element(*HomeLoc.REWARDS_BTN)
        element.click()

    def navigate_Store_Locator_Screen(self):
        element = self.driver.find_element(*HomeLoc.STORE_LOCATOR_TXT)
        element.click()
