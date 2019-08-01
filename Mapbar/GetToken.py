#获取token
import requests
def Gettoken():
    posturl = 'https://wdservice.mapbar.com/ssoapi/user/login?'
    dianhua = '15811060061'
    postdata = ' {"loginName":"'+dianhua+'","autoLogin":"1","captcha": "", "password":"qqqqqq","product":"webUser"}'
    headers = {'Content-Type': 'application/json'}
    reponse = requests.request("post", posturl, data=postdata, headers=headers)
    # print(reponse.text)
    print(type(reponse))
    temp = reponse.json()  # 转换成json格式
    # print(kkk)
    # print(type(kkk))
    # print(kkk['data']['token'])
    ttoken = temp['data']['token']
    #print(ttoken)
    return ttoken
token = Gettoken()
print(token)