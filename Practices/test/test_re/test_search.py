



import re
#从字符串中找到目标字符,在字符串的全文中搜索匹配一次，同样也不会直接返回匹配成功的字符串
str = 'kkkabccba'

result = re.search('abc',str)
print(result.group())


result = re.search('abc*',str)
print(result.group())

result = re.search('abc\D+',str)
print(result.group())