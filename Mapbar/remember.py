import urllib.request
from urllib import request
from urllib import request, parse

#urllib模块get  需要import urllib.request

url = 'http://192.168.0.175:9091/job/query/Z20170822000016'

res = urllib.request.urlopen(url).read()

print(res.decode('utf-8'))


#使用from urllib import request 的GET
url = 'http://192.168.0.175:9091/job/query/Z20170822000016'
res = urllib.request.urlopen(url)
result = res.read().decode('-utf-8')
print(result)





#from urllib import request, parse 的POST
#from urllib import request, parse

posturl = "http://uc.mapbar.com/user/auth?"
postdata={
    "account":'lll',
    "password":'123456',
    "product":'main_site'
 }

data = parse.urlencode(postdata).encode('utf-8')
req = request.Request(posturl, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

print (page)




#参数在url的post
import urllib.request
from urllib import request,parse

a = 'Z201709010000190846'
url = 'http://192.168.0.175:9091/job/del/'+ a

#url = 'http://192.168.0.175:9091/job/del/Z201709010000190846'
print(url)

postdata = {

}
data = parse.urlencode(postdata).encode('utf-8')
req = request.Request(url,data = data)
page = urllib.request.urlopen(req)
res = page.read()
print(res)


import requests
#requests的POST
url = "http://192.168.0.175:9092/add/appkey/"

payload = '{"app_key":"key11111","app_type":"1","app_name":"appkeyName","operate_plat":"1","description":""}'
payload = payload.encode('utf-8')    #如果参数中有中文，则需要这一步进行转换（具体用法见方法3）
response = requests.request("POST", url, data=payload)
print(response.text)


import http.client
#使用http.client的POST
conn = http.client.HTTPConnection("192.168.0.175:9091")

jobname = '中文'    #参数化
straa = '3'        #参数化
payload = '{"jobName":"'+jobname+'","timeType":"'+straa+'","beginDate":"2017-07-10","beginTime":"10:02:01:328","expDate":"2017-10-01","downId":["guid1","guid2"],"idType":"1"}'
payload = payload.encode('utf-8')     #参数有中文，转换为byte传参
conn.request("POST", "/job/add", payload)
data = res.read()

print(data.decode("utf-8"))

#关于split的使用
tar1 = 'title={WiMAX Power Amplifier Design based on Si-LDMOS},author={Nader, Charles and De Carvalho, Nuno Borges},journal={University of Galve, Sweden},year={2006}'
for item in tar1.split('},'):
    print(item)
    print(item.split('={'))

for item in tar1.split('},'):
    if 'auth' in item:      #用来找到自己要的那断，也可以用Charles，等锁定
        print(item.split('={')[1])      #再次分割，并取第二个值

#关于findall的使用
tar2 = 'site sea sue sweet see case sse ssee loses'
k = re.findall(r'\bs\S*e\b',tar2)
print(k)

#关于findall中查找电话号码
dianhua = ['192033','15811060061','2332','3333333','1111111','23131234567890']
tar4 = str(dianhua)
print(tar4)
tem = re.findall(r'\b1\d{10}\b',tar4)
print(tem)

#关于findall中查找定长的字符串
dianhua = ['192033','15811060061','2332','3333333','1111111','23131234567890','aue','abcd','askjf1']

tar4 = str(dianhua)
print(tar4)

tem = re.findall(r'\b[a-zA-Z]{4}\b',tar4)#查询4位的字符串  需要加入数字真的话，可以用这个代替[a-zA-Z0-9]
print(tem)


#把两张list变成dict
list1 = ['a','b','c']
list2 = [1,2,3]

n = dict(zip(list1,list2))
print(n)

#匹配各种电话：其中问号，是指，可能什么都没有
tar = '(021)88776543 010-55667890 02584453362 0571 66345673 15811060061 '
kk = re.findall(r'\d{3,4}[- ]?\d{8}|\(\d{3}\)\d{8}',tar)
print(kk)

#random,随机
str1 = 'gyq fjy hzj ljd'
list1 = ['gyq','hzj','fjy','ljd']
k = random.choice(list1)
j = random.randrange(1,9,3)
m = random.sample(str1,5)
print(k,j,m)


#交换位置
a = 3
b = 4
a,b=b,a
print(a,b)