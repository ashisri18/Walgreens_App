import xlrd
import xlsxwriter
from com.generic_lib.report import *
import sys, traceback
import os

class ExcelSheet():
    testcaseid_array = []
    testcasestatus_array = []
    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook(Report.read_excel_path+"TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            for current_Row in range(worksheet.nrows):
                current_Id = str(worksheet.row(current_Row)[0])[7:18]
                if current_Id == testCaseId:
                    for current_cell in range(worksheet.ncols):
                        data.append(worksheet.cell_value(current_Row, current_cell))
                    break
            return data

        #except:
            traceback.print_exception("there is some exception.")


    # def write_data(self):
    #
    #     os.chdir(Initilization.log_path)
    #     workbook = xlsxwriter.Workbook(Initilization.path+"Report\Excel_Sheet\Status"+"-" + Initilization.now + ".xlsx")
    #     worksheet = workbook.add_worksheet()
    #     row = 0
    #     col = 1
    #     testCaseId = []
    #     count = 0
    #     with open('Logs.txt') as infile:
    #         value = "TestCase_"
    #         for line in infile:
    #             if value in line:
    #                 testCaseId = line.split(":")[2]
    #                 print testCaseId
    #                 testCaseId = testCaseId.split("=")[0]
    #                 testStatus = testCaseId.split("=")[1]
    #                 # valueStatus = "passed"
    #                 # testStatus = lientestID.split(" ")[2]
    #                 print (testCaseId + "==" + testStatus)
    #                 worksheet.write(count, 0, testCaseId)
    #                 worksheet.write(count, 1, testStatus)
    #                 count = count + 1
    #                 print count
    #                 # row +=1
    #                 # col+=1
    #         workbook.close()

    def update_status_array(self, testCaseId, test_status):
        self.testcaseid_array = self.testcaseid_array.append(testCaseId)
        print(self.testcaseid_array)
        self.testcasestatus_array = self.testcasestatus_array.append(test_status)
        print(self.testcasestatus_array)
        return self.testcaseid_array, self.testcasestatus_array

    def writeExcel(self):
        report = Report()
        # print ("i am in write excel")
        os.chdir(report.excel_report_path())
        workbook = xlsxwriter.Workbook('excel_status.xlsx')
        worksheet = workbook.add_worksheet()
        count = 0
        # testcaseid = []
        # testcasestatus = []
        # self.testcaseid_array.append(testCaseId)
        # print self.testcaseid_array
        # self.testcasestatus_array.append(test_status)
        # testCaseIdlist = id_list
        # testStatuslist = status_list
        for testCaseId in self.testcaseid_array:
            worksheet.write(count, 0, self.testcaseid_array[count])
            worksheet.write(count, 1, self.testcasestatus_array[count])
            count = count + 1
        # print ("i am leaving write excel")
        # print count
        workbook.close()

