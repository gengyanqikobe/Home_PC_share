
 # 使用匹配成功的字符串替换成指定的字符串，参数依次为正则表达式，匹配成功后要去替换的字符串，原字符串，替换次数


import re

str = 'abcabcabc'

result = re.sub('a','9999',str,3)

print(result)


result = re.sub('abc','ccc',str,2)

print(result)