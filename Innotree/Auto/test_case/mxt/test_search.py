#coding=utf-8

#test_search为企业查询和suggest接口
import unittest
from Innotree.Auto.common import url_post,Wrong_msg,url_get

class Search(unittest.TestCase):
    global dict_response ,a
    a = []

    def search_by_chanpin(self):
        #根据产品查询企业
        json_par = {

            "source":"TRUSTRAER",
            "type":3,
            "andOr":1,
            "page":1,
            "pageSize":10,
            "keywords":"茶叶",
            "tags":[],
            "operation":{"status":""},
            "reg":{"capital":{"code":"","max":"","min":""},"regTime":{"code":"","max":"","min":""},"area":{"province":"","city":"","district":""}},
            "advanced":{"patent":""},
            "trustFilter":{"corpTrustType":"","latestTradeDate":"","majorExportRegion":"","currency":""},
            "direction":1
        }
        self.url = 'http://www.trustrader.cn/api/paas/search/unify/corp'

        response = url_post(self.url,json_par)
        dict_response = eval(response.text)

        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.total = dict_response['data']['total']
            #print(type(self.total),self.total)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.total,0,msg="按产品查询企业接口数据异常 "+ response.url)

    def search_by_biaoqian(self):
        #根据产品标签搜索
        json_par = {

            "source":"TRUSTRAER",
            "type":2,
            "andOr":1,
            "page":1,
            "pageSize":10,
            "keywords":"",
            "tags":["科学健康","科学"],
            "operation":{"status":""},
            "reg":{"capital":{"code":"","max":"","min":""},"regTime":{"code":"","max":"","min":""},"area":{"province":"","city":"","district":""}},
            "advanced":{"patent":""},
            "trustFilter":{"corpTrustType":"","latestTradeDate":"","majorExportRegion":"","currency":""},
            "direction":1
        }
        self.url = 'http://www.trustrader.cn/api/paas/search/unify/corp'

        response = url_post(self.url,json_par)
        dict_response = eval(response.text)
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.total = dict_response['data']['total']
            #print(type(self.total),self.total)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.total,0,msg="按标签查询企业接口数据异常 "+ response.url)


    def search_by_name(self):
        #根据公司名字搜索
        json_par = {

            "source":"TRUSTRAER",
            "type":1,
            "andOr":1,
            "page":1,
            "pageSize":10,
            "keywords":"北京一",
            "tags":[],
            "operation":{"status":""},
            "reg":{"capital":{"code":"","max":"","min":""},"regTime":{"code":"","max":"","min":""},"area":{"province":"","city":"","district":""}},
            "advanced":{"patent":""},
            "trustFilter":{"corpTrustType":"","latestTradeDate":"","majorExportRegion":"","currency":""},
            "direction":1
        }

        self.url = 'http://www.trustrader.cn/api/paas/search/unify/corp'

        response = url_post(self.url,json_par)
        dict_response = eval(response.text)
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.total = dict_response['data']['total']
            #print(type(self.total),self.total)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.total,0,msg="按名称查询企业接口数据异常 "+ response.url)


    def suggest_by_biaoqian(self):
        json_par = {
            "type":2,
            "keyword":"我爱我"
        }
        self.url = 'http://www.trustrader.cn/api/paas/search/suggest'

        response = url_get(self.url,json_par)
        dict_respone = eval(response.text)
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_respone['data']
            #print(type(self.data),self.data)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="按产品suggest接口数据异常 "+ response.url)

    def suggest_by_name(self):
        json_par = {
            "type":0,
            "keyword":"北京科技"
        }
        self.url = 'http://www.trustrader.cn/api/paas/search/suggest'

        response = url_get(self.url,json_par)
        dict_response = eval(response.text)
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)

        try:
            self.data = dict_response['data']
            #print(type(self.data),self.data)
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="按名称suggest接口数据异常 "+ response.url)

