


import unittest

from Practices.apiPort_practice.testCase import test_park_list

suite = unittest.TestSuite()

suite.addTest(test_park_list.Park_List('park_list'))






if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)