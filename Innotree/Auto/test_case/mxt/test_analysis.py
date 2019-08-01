

#test_analysis.py贸信通-企业查询-企业画像模块和外贸信息模块
import unittest
from Innotree.Auto.common import url_get

class Analysis(unittest.TestCase):
    #定义全局变量，错误返回信息和临时参数接收
    global Wrong_msg,dict_response,par,a
    #空列表用于数据判断
    a=[]
    Wrong_msg = '接口未返回数据  url='

    par = {
        "corpId":"16327190365788238362"
    }
    def analysis_options(self):
        #企业画像-区域分析接口
        self.url ='http://www.trustrader.cn/api/trade/corp/analysis/region/options'
        response = url_get(self.url,par)
        print(response.url)
        dict_response = eval(response.text)

        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_response['data']
            #print(self.data)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="区域分析接口数据为空"+ response.url)


    def analysis_cate(self):
        #企业画像-产品类别分析
        self.url = 'http://www.trustrader.cn/api/trade/corp/analysis/cate'

        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_response['data']
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="产品类别分析接口数据为空 " + response.url)

    def analysis_country(self):
        #企业画像-出口国分析
        self.url = 'http://www.trustrader.cn/api/trade/corp/analysis/country'

        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_response['data']
            #print(self.data)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="出口国分析接口数据为空 " + response.url)



    def trade_data(self):
        #外贸信息-外贸数据接口
        self.url = 'http://www.trustrader.cn/api/trade/corp/trade/hs/data'
        par1 = {
            'corpId':'16327190365788238362',
            'page':'1',
            'pageSize':'10'
        }

        response = url_get(self.url,par1)
        dict_response = eval(response.text)
        #print(dict_response)

        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.count = dict_response['data']['count']
            #print(self.count)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.count,0,msg="外贸数据接口数据为空 " + response.url)