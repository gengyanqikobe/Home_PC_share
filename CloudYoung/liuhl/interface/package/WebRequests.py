# -*- coding: utf-8 -*-

import requests
import json
import configparser
from os.path import abspath, dirname

class WebRequests:
    def get(self, url, para, headers):
        try:
            r = requests.get(url, params=para, headers=headers)
            print('获取返回的状态码', r.status_code)
            json_r = r.json()
            print('json类型转化成python数据类型', json_r)
        except BaseException as e:
            print('请求失败！', str(e))

    def post(self, url, para, headers):
        try:
            r = requests.post(url, data=para, headers=headers)
            print('获取返回的状态码', r.status_code)
            json_r = r.json()
            print('json类型转化成python数据类型', json_r)
        except BaseException as e:
            print('请求失败！', str(e))

    def post_json(self, url, para, headers):
        try:
            data = para
            data = json.dumps(data)
            r = requests.post(url, data=data, headers=headers)
            print("获取返回的状态码", r.status_code)
            json_r = r.json()
            print('json类型转化成python数据类型', json_r)
        except BaseException as e:
            print('请求失败！', str(e))

if __name__ == '__main__':
    # url = 'http://openapi.qa.cloud-young.cn/scancarserver/scancar/v1/scanCar/getStyleConfigList'
    # para = {'serialId': 3, 'dealerId': 10001, 'styleId': 9}
    # hearders = {}

    '''获取当前文档相对路径'''
    file_path = dirname(abspath(__file__)) + '/conf.ini'

    '''从配置文件中获得参数信息，获得的数据类型为str，
    按需转换，这里使用eval()，作用是将字符串str当成有效的表达式来求值并返回计算结果'''
    config = configparser.ConfigParser()
    config.read(file_path)
    url = config.get('Parameter', 'url')
    para = eval(config.get('Parameter', 'para'))
    hearders = eval(config.get('Parameter', 'hearders'))

    '''数据类型转换方式json，后续尝试'''

    q = WebRequests()

    q.get(url, para, hearders)
    q.post(url, para, hearders)      #get接口不支持post
    q.post_json(url, para, hearders)      #get接口不支持post