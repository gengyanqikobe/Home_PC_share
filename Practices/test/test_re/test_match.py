


import re



result = re.match('b?','bac')

#如果为空的话，输出报错,match是从开头匹配
print(result.group())

#\D,代表非数字,一个符号一个字符
result = re.match('b\D','bba')
print(result.group())


#加上“+”，就可以显示多个
result = re.match('\D+','bba')
print(result.group())

