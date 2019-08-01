
#获取BI系统cookie
import requests


def get_Cookie():

    url = 'http://10.64.6.35/bi/work/home/verify.do?username=17692357081&password=123456'

    respone = requests.get(url = url)

    cookies = respone.cookies
    cookies_str = str(cookies)
    cookies_temp = cookies_str.split('<Cookie ')[1] #进行两次切割拿到想要的cookie
    cookie = cookies_temp.split(' for ')[0]
    return cookie





#get_Cookie()