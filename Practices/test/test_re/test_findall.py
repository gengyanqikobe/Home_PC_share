



import re


str = 'abcd1bcd2bcd3a'

result = re.findall('abc',str)

print(result)   #可以直接输出匹配到的字符串


result = re.findall('bcd\d',str)

print(result)
