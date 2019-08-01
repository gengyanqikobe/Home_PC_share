#coding=utf-8
import requests
import json

#本文件包含get请求方式，post请求方式，以及一些通用的变量
def url_get(url,par):
    headers = {
        'accessToken':'fc8a933e42f8993861820ebf05717c54dead2152530ad93af014bc2c19c6ba4667de96aa56003ddd4d8d42eff7d79254fa7b8a9e42ca613db93c002f959272bb801f17920f33abfd19d1cc37a22cfe9f'
    }

    response = requests.get(url = url, params= par ,headers =headers)
    #print(response.url)


    return response
    # print(type(dict_response))

# par = {
#     'corpId':'16327190365788238362',
#     "page":'1'
# }
# url_get('http://www.trustrader.cn/api/paas/corp/detail/patents',par)


def url_post(url,json_par):
    headers = {
         'Content-Type':'application/json',

        'accessToken':'fc8a933e42f8993861820ebf05717c54dead2152530ad93af014bc2c19c6ba4667de96aa56003ddd4d8d42eff7d79254fa7b8a9e42ca613db93c002f959272bb801f17920f33abfd19d1cc37a22cfe9f'
    }

    response = requests.post(url,data=json.dumps(json_par),headers = headers)
    #print(response.text)

    return response


Wrong_msg = '接口未返回数据  url='
#
# url = 'http://www.trustrader.cn/api/paas/search/unify/corp'
# json_par = {
#     "source":"TRUSTRAER",
#     "type":3,
#     "andOr":1,
#     "page":1,
#     "pageSize":10,
#     "keywords":"茶叶",
#     "tags":[],
#     "operation":{"status":""},
#     "reg":{"capital":{"code":"","max":"","min":""},"regTime":{"code":"","max":"","min":""},"area":{"province":"","city":"","district":""}},
#     "advanced":{"patent":""},
#     "trustFilter":{"corpTrustType":"","latestTradeDate":"","majorExportRegion":"","currency":""},
#     "direction":1
# }
#
# url_post(url,json_par)