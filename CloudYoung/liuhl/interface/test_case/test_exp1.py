# -*- coding: utf-8 -*-
import requests
import unittest

class test_hexp(unittest.TestCase):
    '''把接口封装成一个接口类，下面的每个方法对应一条接口测试用例'''
    url_g = 'http://openapi.qa.cloud-young.cn/scancarserver/scancar/v1/scanCar/getStyleConfigList'

    def test_exp2(self):

        print('实例exp')

if __name__ == '__main__':
    unittest.main()