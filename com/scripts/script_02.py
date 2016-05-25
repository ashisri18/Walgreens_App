from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sports_method import *
from com.generic_lib.excel_sheet import *
from selenium.common.exceptions import *
from com.generic_lib.report import *
import traceback

class Script02_Sports(Initilization, ExcelSheet):
    testCaseId = "TestCase_02"
    test_status = None

    def test_02_buy_jersey(self):
        test_method_name = self._testMethodName
        # initilization = Initilization()
        report = Report()
        try:
            home_page = HomePage(self.driver)
            sport = Sport(self.driver)
            logging.info('Now in Sport Script')

            home_page.navigate_sports()
            sport.buy_jerseys()
            self.test_status = "Pass"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)

        except WebDriverException:
            logging.error('Exception raised in method - ' + test_method_name)
            # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # self.driver.save_screenshot(
            #     Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
            self.driver.save_screenshot(
                 report.screenshot_path() + test_method_name + "-" + report.now + ".png")
            traceback.print_exc()
            self.test_status = "Fail"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)
            raise WebDriverException