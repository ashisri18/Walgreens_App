from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
from com.generic_lib.report import *
from com.generic_lib.excel_sheet import *
import logging

class Script01_SignIn(Initilization, ExcelSheet):

    testCaseId = "TestCase_01"
    sheetName = "SignInData"

    def test_01_sign_in(self):
        report = Report()
        test_method_name = self._testMethodName
        try:
            home_page = HomePage(self.driver)
            sign_in_page = SignInPage(self.driver)

            home_page.navigate_signin_page()
            sign_in_page.enter_email_id(self.testCaseId, self.sheetName)
            sign_in_page.enterPassword(self.testCaseId, self.sheetName)
            sign_in_page.clickSignInBtn()
            sign_in_page.display_error_msg()
            sign_in_page.verifyErrorMsg()
            sign_in_page.sign_in_with_google()
            sign_in_page.enter_gmail_id(self.testCaseId, self.sheetName)
            sign_in_page.enter_gmail_password(self.testCaseId, self.sheetName)
            sign_in_page.click_gmail_signin_button()
            sign_in_page.verify_jabong_loggedin()

            logging.info("*****Congratulations we have successfully passed this Login to Jabong script.*****")
            self.test_status = "Pass"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)

        except AssertionError:
            logging.error('Exception raised in method - '+ test_method_name)
            # now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                report.screenshot_path() + test_method_name + "-" + report.now + ".png")
            traceback.print_exc()
            self.test_status = "Fail"
            logging.info(self.testCaseId + "=" + self.test_status)
            self.update_status_array(self.testCaseId, self.test_status)
            raise AssertionError


# if __name__ == "__main__":
#     unittest.main()