


#test_trade.py为贸易数据模块相关接口
#coding=utf-8
import unittest

from Innotree.Auto.common import url_get,Wrong_msg


class Trade(unittest.TestCase):

    global a,json_par
    #a为空列表，进行判断使用
    a = []


    def trade_list_by_hs_area(self):#出口贸易流向分析接口
        json_par = {
        "hsCodes":"A1,A2",
        "areaIds":"1000,2000,3000,4000,5000"
        }

        self.url = "http://www.trustrader.cn/api/trade/trade/area/hs/count/list_by_hs_area"

        response = url_get(self.url,json_par)
        #print(response.url)
        dict_response = eval(response.text)
        #判断是否是网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_response['data']
            #print(self.data)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="出口贸易流向分析接口数据异常 "+ response.url)


    # def trade_export(self):
    #     self.url = 'http://www.trustrader.cn/api/trade/trade/area/hs/count/export_by_hs_area'
    #     #为入参增加一个字段
    #     json_par.update(statisticType=0)
    #     print(json_par)
    #     response = url_get(self.url,json_par)
    #     #dict_response = eval(response.text)
    #     #判断是否是网关错误
    #     #self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
    #


    #以下是供应商画像相关接口

    def trade_supplier_list(self):

        json_par = {
        "hsCode":"A1",
        "transitAreaId":"110",
        "toAreaId":"116",
        "page":"1"
        }

        self.url = 'http://www.trustrader.cn/api/trade/trade/area/hs/supplier/list'

        response = url_get(self.url,json_par)
        dict_response = eval(response.text)
        #print(dict_response)

        #判断是否是网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.count = dict_response['data']['count']
            #print(type(self.count),self.count)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.count,0,msg="供应商画像接口数据异常 "+ response.url)

    #供应商画像导出先不做
