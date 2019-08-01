


import re


str = 'pythonpython23'


result = re.search('(python)python(\d{1,3})',str)

print(result.groups())
print(result.group())

wangzhi = 'www.baidu1.com'

result = re.search('www\.(\w{,})\.com',wangzhi)

print(result.groups())



str = 'python'
#groups()等同于group(1,2)
result = re.search('(y)th(o)n',str)
print(result.groups())
print(result.group(0))#参数0无效
print(result.group(1))
print(result.group(2))
print(result.group(1,2))


