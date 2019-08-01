import urllib.request
import requests

response = urllib.request.urlopen('http://baidu.com',timeout=1)
print(response.read())

response1 = requests.get(url='http://baidu.com',params=None,timeout = 1)
print('requeset.get:',response1.cookies)