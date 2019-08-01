import unittest
from unitest_dealer.test_dealerfunction import TestDealerFunction
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestDealerFunction('test_login')]
    suite.addTests(tests)

    with open('dealer_report.html','wb') as f:
        runner = HTMLTestRunner(stream=f,title='dealer_report',description='经销商dealer登录接口',verbosity=0)
        runner.run(suite)