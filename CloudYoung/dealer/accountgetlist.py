from dealer import dealerlogin
from urllib import parse,request

cookie = dealerlogin.login()
#print(cookie)

url = 'http://dealer.qa.cloud-young.cn/account/getList'
postdata = {
    "mobile" : "",
    "accountName":"小",
    "isLock":"0",
    "roleId":"",
    "pageNun":"1",
    "pageSize":"10"

}
headers = {"cookie": cookie}
data = parse.urlencode(postdata).encode('utf-8')
req = request.Request(url,data = data,headers = headers)
page = request.urlopen(req).read()
page = page.decode('utf-8')
print(page)

