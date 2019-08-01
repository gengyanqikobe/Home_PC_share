#dealer-login
from urllib import parse,request
from http import cookiejar
def login():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)


    url  = 'http://mmc.qa.cloud-young.cn/userLogin'

    postdata = {
        "userName":"admin",
        "password":"123456"

    }
    data = parse.urlencode(postdata).encode('utf-8')
    req = request.Request(url,data = data)
    response = opener.open(req)
    #page = request.urlopen(req).read()
    #page = page.decode('utf-8')
    #print(cookie)
    #print(response)
    for item in cookie:
        t_cookie = str(item)

    #print(t_cookie)
    list_split =[]
    for item in t_cookie.split(' '):
        #print(item)
        if 'castoken=' in item:
            #print(item)

            for item1 in item.split('castoken='):

                list_split.append(item1)


    tt_cookie = list_split[1]#得到castonken的值
    #print('ttcookie:',tt_cookie)
    return tt_cookie



#headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#res = requests.request('post',url,data = postdata,headers = headers)

    #print(page)
a =login()
print(a)
