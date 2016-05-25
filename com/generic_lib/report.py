import os
import logging
from datetime import datetime

class Report:
    dir = os.path.dirname(__file__)
    path = dir[:len(dir) - 32]
    read_excel_path = path+"Walgreens_App\\"
    print(path)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # def log_path(self):
    log_path = path+"Framework_Reports\Logs\\"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logging.basicConfig(level=logging.INFO, filename=log_path + "Test" + "-" + now + ".log")
        # return log_path

    def html_report_path(self):
        html_report_path = self.path +"Framework_Reports\HTML_Reports\\"
        if not os.path.exists(html_report_path):
            os.makedirs(html_report_path)
        return html_report_path

    def screenshot_path(self):
        screenshot_path = self.path+"Framework_Reports\Screenhots\\"
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        return screenshot_path

    def excel_report_path(self):
        excel_report_path = self.path + "Framework_Reports\Excel_Reports\\"
        if not os.path.exists(excel_report_path):
            os.makedirs(excel_report_path)
        return excel_report_path



# import unittest
# class TestResultX(unittest.TestResult):
#     def startTest(self, test):
#         print('# blip')
#         unittest.TestResult.startTest(self, test)
#
#     def stopTest(self, test):
#         print('# blop')
#         unittest.TestResult.stopTest(self, test)
#
#     def startTestRun(self):
#         print('# blep')
#         unittest.TestResult.startTestRun(self)
#
#     def stopTestRun(self):
#         print('# blap')
#         unittest.TestResult.stopTestRun(self)
#
# class TestCaseX( unittest.TestCase ):
#     def test_nonsense(self):
#         print( '# wotcha' )
#         self.assertTrue( False )
#
#     def run( self, test_result=None ):
#         print( '# spoons starting...')
#
#         test_result = TestResultX()
#         unittest.TestCase.run( self, test_result )
#
#         print( '# ...spoons ended, tr %s' % ( test_result,  ) )
#
# unittest.main()

# from selenium.common.exceptions import *
# from com.generic_lib.initilization import *
# import traceback
#
# class NoSuchElementException(WebDriverException):
#     logging.error('NoSuchElementException raised in method - ' + test_method_name)
#     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     self.driver.save_screenshot(
#         Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
#     traceback.print_exc()
#     raise WebDriverException