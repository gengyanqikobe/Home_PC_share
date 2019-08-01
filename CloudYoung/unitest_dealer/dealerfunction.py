from urllib import parse,request

def login(username,password):
    url = 'http://dealer.qa.cloud-young.cn/dologin'
    postdata = {
        "userName":username,
        "password":password
    }
    data = parse.urlencode(postdata).encode('utf-8')
    req = request.Request(url,data = data)
    page = request.urlopen(req).read().decode('utf-8')
    print(page)
    for item in page.split(','):
        #print(item)
        if '"result":'in item:
            result = item.split(':')[1]
    return result




#print(login(10001,123456))