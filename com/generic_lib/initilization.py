import unittest
import time
# from selenium import webdriver
from appium import webdriver
import Config
import logging
from com.generic_lib.excel_sheet import *
from datetime import datetime
import sys
import os

class Initilization(unittest.TestCase, ExcelSheet):
    # dir = os.path.dirname(__file__)
    # read_excel_path = dir[:len(dir)-15]
    # print(path)
    # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # log_path = path+"Report\Logs\Test"+"-" + now + ".log"
    # logging.basicConfig(level=logging.INFO,filename = log_path)



    excel_sheet = ExcelSheet()
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Redmi-2'
        desired_caps['noReset'] = 'true'
        desired_caps['app'] = "D:\CBT_Automation\Ashish\Apk's\com.usablenet.mobile.walgreen-1.apk"
        desired_caps['appPackage'] = 'com.usablenet.mobile.walgreen'
        desired_caps['appActivity'] = '.AppStart'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

        # global path

        # if Config.Browser.lower() == 'Firefox'.lower():
        #     self.driver = webdriver.Firefox()
        #     logging.info('Firefox browser launched.')
        #
        # elif Config.Browser.lower() == 'Chrome'.lower():
        #     chromeDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\chromedriver.exe"
        #     self.driver = webdriver.Chrome(chromeDriver)
        #     logging.info('Chrome browser launched.')
        # else:
        #     ieDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\IEDriverServer.exe"
        #     self.driver = webdriver.Ie
        # #self.driver = webdriver.Firefox()
        # logging.info('Inside Setup method')
        # self.driver.get(Config.URL)
        # logging.info('Jabong Application Launched.')
        # self.driver.maximize_window()
        # time.sleep(3)
        # self.driver.implicitly_wait(5)

    def tearDown(self):
        logging.info("Inside TearDown Method.")
        self.driver.quit()

    def test_tap_on_photo(self):
        self.driver.find_element_by_id("btn_home_photo")
        time.sleep(5)

    # def tearDownClass(cls):
    #     cls.excel_sheet.writeExcel()


# if __name__ == "__main__":
#     unittest.main()