import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os

#加载测试接口
from test_case.test_getStyleConfigList import test_getStyleConfigList
from test_case.test_exp1 import test_hexp

#构造测试集
suite = unittest.TestSuite()

#添加测试用例到测试集中,注意执行顺序
suite.addTest(test_getStyleConfigList('test_getStyleConfigList_normal'))
suite.addTest(test_hexp('test_exp2'))
suite.addTest(test_getStyleConfigList('test_getStyleConfigList_str'))

#添加用例方式2，添加test_getStyleConfigList类中的所有test_用例
# suite2 = unittest.TestLoader().loadTestsFromTestCase(test_getStyleConfigList)
# unittest.TextTestRunner(verbosity=2).run(suite2)

#添加用例方式3
# suite3 = unittest.makeSuite(test_getStyleConfigList)
# runner.run(suite3)

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(suite)

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    path = os.path.abspath('..')
    test_report = path + '/test_report'
    filename = test_report + '/' + now + 'test_result.html'
    fp = open(filename, 'wb')

    # # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="xxx接口测试报告",
                            description="测试用例执行情况：")

    # 运行测试
    runner.run(testunit)
    fp.close()