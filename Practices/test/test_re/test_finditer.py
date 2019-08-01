


import re

str = '11Python,twopython22,Three33pythoN'


result = re.finditer('(\d+)(python)',str)

for res in result:
    print(res.groups())
    print(res.group(1),res.group(2))

#
for res in result:
    print(res.groups())



result = re.findall('\D+',str)
print(result)