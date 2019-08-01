# -*- coding: utf-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner
from uniteset_lianxi.test_mathfunction import TestMathFuncion

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFuncion('test_add'),TestMathFuncion("test_mul"),TestMathFuncion("test_sub"),TestMathFuncion('test_div')]
    suite.addTests(tests)


    #写入到一个txt中
    # with open("mathfuction_report.txt",'a') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)

    with open("_report_html.html",'ab')as f:
        runner = HTMLTestRunner(stream=f,title="mathfunction_report",description="此为测试练习",verbosity=2)
        runner.run(suite)