from com.scripts.script_03 import *
from com.scripts.script_02 import *
from com.scripts.script_01 import *
import unittest
from com.generic_lib.report import *
import HTMLTestRunner

class Suite(unittest.TestCase):

    def test_main(self):
        report = Report()
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(Script01_SignIn),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script02_Sports),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script03_Men)])

        outputfile = open(report.html_report_path() + "TestReport" + "-" + report.now + ".html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile, verbosity=2,title='Execution Report',description='Suite Run')
        runner.run(self.suite)