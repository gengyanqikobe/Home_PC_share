# -*- coding: utf-8 -*-
import requests
import unittest
from package.WebRequests import *

class MyTest(unittest.TestCase):
    '''封装测试环境的初始化和还原的类'''
    def setUp(self):
        '''存放数据库联接的初始化信息等'''
        print('start test_t')
        pass

    def tearDown(self):
        '''与setUp对应'''
        print('end test_t')
        pass

class test_getStyleConfigList(MyTest):
    '''把接口封装成一个接口类，下面的每个方法对应一条接口测试用例，以上信息会在报告中显示'''
    url_g = 'http://openapi.qa.cloud-young.cn/scancarserver/scancar/v1/scanCar/getStyleConfigList'

    def test_getStyleConfigList_normal(self):
        '''正确的参数'''
        payload_normal = {'serialId': 3, 'dealerId': 10001, 'styleId': 9}

        '''发送请求'''
        r = requests.get(url=self.url_g, params=payload_normal)

        '''打印请求url、请求状态码、请求报文'''
        print('请求的url是：',r.url)
        print('请求返回的状态码是：',r.status_code)
        print('请求返回的内容是：', r.text)
        print(r.status_code == requests.codes.ok)

        # '''封装：调用WebRequests内get方法'''
        # hearders = {}
        # r = WebRequests()
        # r.get(self.url_g, payload_normal, hearders)

        '''后续补充其他断言，数据验证等'''

    def test_getStyleConfigList_str(self):
        '''输入str类型参数'''
        payload_normal = {'serialId': 'abc', 'dealerId': 10001, 'styleId': 9 }

        '''发送请求'''
        r = requests.get(url=self.url_g, params=payload_normal)

        '''打印请求url、请求状态码、请求报文'''
        print('请求的url是：', r.url)
        print('请求返回的状态码是：', r.status_code)
        print(r.status_code == requests.codes.ok) # '''返回false'''
        r.raise_for_status()   #'''非200响应报异常'''

if __name__ == '__main__':
    unittest.main()