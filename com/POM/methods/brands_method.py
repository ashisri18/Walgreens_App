from com.POM.locators.shop_products_loc import *
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class InternationalGas(BasePage):

    def click_gas(self):
        self.driver.find_element
