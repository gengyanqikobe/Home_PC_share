#dealer-login
from urllib import parse,request
from http import cookiejar
def login():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)


    url  = 'http://dealer.qa.cloud-young.cn/dologin'

    postdata = {
        "userName":"10001",
        "password":"123456"

    }
    data = parse.urlencode(postdata).encode('utf-8')
    req = request.Request(url,data = data)
    response = opener.open(req)
    #page = request.urlopen(req).read()
    #page = page.decode('utf-8')
    #print(cookie)
    #print(response)
    t_cookie =str(cookie)

    #print(t_cookie)

    list_split =[]
    for item in t_cookie.split(' '):
        list_split.append(item)
    tt_cookie = list_split[1]
    #print(tt_cookie)
    return tt_cookie

#headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#res = requests.request('post',url,data = postdata,headers = headers)

    #print(page)
login()