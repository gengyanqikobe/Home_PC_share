import unittest
import HTMLTestRunner
import os
from Practices.readConfig import proDir
from Practices.common.configEmail import MyEmail

class ALLTEST:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(proDir,'result')
        self.caseListFile = os.path.join(proDir,'caselist.txt')
        self.caseFile = os.path.join(proDir,'testCase')
        self.caseList = []
        self.email = MyEmail.get_email()


    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != ' 'and not data.startswith('#'):
                self.caseListFile.append('\n','')
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            case_file = os.path.join(proDir,'testCase')
            print(case_file)
            case_name = case.split('/')[-1]
            print(case_name + '.py')
            discover = unittest.defaultTestLoader.discover(case_file,pattern=case_name+'.py',top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                print("测试开始")
                fp = open(resultPath,'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                print("没有case可以测试")
        except Exception as ex:
            print(ex)

        finally:
            print("测试结束")
            fp.close()
            self.email.send_mail()

if __name__ == '__main__':
    obj = ALLTEST
    obj.run()
