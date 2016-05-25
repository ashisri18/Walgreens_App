from com.generic_lib.initilization import *
from com.generic_lib.listener import *
from com.POM.methods.home_method import *
from com.POM.methods.men_method import *
from com.POM.methods.sports_method import *
from com.generic_lib.excel_sheet import *
from com.generic_lib.report import *
from selenium.common.exceptions import *
import logging
import traceback

class Script03_Men(Initilization, ExcelSheet):
    testCaseId = 'TestCase_03'
    def test_03_buy_blazers(self):
        report = Report()
        test_method_name = self._testMethodName
        try:
            home_page = HomePage(self.driver)
            clothing = Clothing(self.driver)

            logging.info('Now in Men Script')
            home_page.navigate_men()
            clothing.click_suits_blazers()
            clothing.scroll_down()
            clothing.click_filter_slim()
            clothing.open_blazer()
            clothing.select_size()
            clothing.click_add_to_bag()
            clothing.click_bag_icon()
            clothing.click_remove_button()

            self.test_status = "Pass"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)


        except WebDriverException:
            logging.error('Exception raised in method - ' + test_method_name)
            # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                report.screenshot_path() + test_method_name + "-" + report.now + ".png")
            traceback.print_exc()
            self.test_status = "Fail"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)
            raise WebDriverException
