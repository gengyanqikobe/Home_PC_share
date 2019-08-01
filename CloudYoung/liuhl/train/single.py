# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner

def add(a, b):
    return a+b

class Math(unittest.TestCase):

    '''测试add'''
    def test_add(self):
        """Test method add(a,b)"""
        print('add')
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # 定义一个测试容器
    test = unittest.TestSuite()

    # 将测试用例，加入到测试容器中
    test.addTest(Math("test_add"))

    # 运行测试用例
    runner = HTMLTestRunner.HTMLTestRunner()
    runner.run(test)