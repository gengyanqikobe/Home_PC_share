


##test_detail.py为贸信通-企业查询-工商信息模块
import unittest
from Innotree.Auto.common import url_get

class Detail(unittest.TestCase):
    #定义全局变量错误信息，临时的字典格式返回值参数,入参par

    global Wrong_msg,dict_response,par,a
    a = []

    Wrong_msg = '接口未返回数据  url='
    par = {
            'corpId':'16327190365788238362'
        }

    def detail_base(self):
        #企业查询下中工商信息里面的基本信息
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/base'


        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)


        try:

            self.corpName = dict_response['data']['corpName']
            self.capital = dict_response['data']['capital']
            self.address = dict_response['data']['address']
        except Exception as e:
            print(Wrong_msg+ response.url)
        else:
            #取公司名称判断是否为空
            self.assertNotEqual(self.corpName,'',msg="公司名称为空 "+response.url)
            #判断资金是否为空
            self.assertNotEqual(self.capital,'',msg="资金为空 "+response.url)
            #判断公司地址是否为空

            self.assertNotEqual(self.address,'',msg='地址为空 '+response.url)

        # self.issuedDate = response['data']['issuedDate']
        # self.assertNotEqual(self.issuedDate,"2017-07-06",msg='地址为空'+self.url)

    def detail_teams(self):
        #企业查询下中工商信息里面的团队
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/teams'
        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:

            self.memberName = dict_response['data'][0]['memberName']
        except Exception as e:
            print(Wrong_msg+ response.url)
        else:
            self.assertEqual(self.memberName,'文琦',msg='团队信息数据异常 '+response.url)

    def detail_patents(self):
        #企业查询下中工商信息里面的专利信息
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/patents'
        par1 = {
            "corpId":"16327190365788238362",
            "page":'1'
        }

        response = url_get(self.url,par1)
        dict_response =eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:
            self.patentId = dict_response['data']['data'][0]['patentId']
        except Exception as e:
            print(Wrong_msg+ response.url)
        else:
            self.assertEqual(self.patentId,'PIDCNA02017052400000000106699115O0KCC0H011222',msg='专利信息数据为空 ' + response.url)

    def detail_competitions(self):
        #企业查询下中工商信息里面的竞品分析
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/competitions'
        par2 = {
            "corpId":"16327190365788238362",
            "page":'1',
            "pageSize":'10'
        }
        response = url_get(self.url,par2)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:
            self.corpId = dict_response['data']['data'][0]['corpId']
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.corpId,'',msg="竞品信息异常" + response.url)


    def detail_judgements(self):
        #企业查询下中工商信息里面的裁判文书
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/judgements'
        par3 = {
            "corpId":"16327190365788238362",
            "page":'1'
        }
        response = url_get(self.url,par3)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:
            self.judgeCourt = dict_response['data']['data'][0]['judgeCourt']
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.judgeCourt,'',msg="裁判文书数据异常" + response.url)

    def detail_tags(self):
        #企业查询下中工商信息里面企业标签
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/tags'
        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:
            self.data = dict_response['data']
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="企业标签为空"+response.url)

    def detail_finances(self):
        #企业查询下中工商信息里面融资信息
        self.url = 'http://www.trustrader.cn/api/paas/corp/detail/finances'
        response = url_get(self.url,par)
        dict_response = eval(response.text)
        #判断是否网关错误
        self.assertNotIn(response.status_code,[400,401,403,500,502],msg="网关服务报错"+str(response.status_code) +response.url)
        try:
            self.data = dict_response['data']
        except Exception as e:
            print(Wrong_msg + response.url)
        else:
            self.assertNotEqual(self.data,a,msg="融资信息为空"+response.url)




if __name__ =="__main__":
    unittest.main()