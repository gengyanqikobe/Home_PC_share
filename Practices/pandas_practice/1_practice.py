



#

from  pandas import Series
import pandas as pd

#可以手动修改index，或者默认
s = Series([1,22,3])
s.index=(1,2,3)

print(s[2])
print(s)
print(s.index)
print('+++++++++++++++++++++++++++++++++++++++++')

#可以是这种形式，加上index


s2  = Series(['kkk','bbb','cccc'],index=[1,2,3])
print(s2)

print('+++++++++++++++++++++++++++++++++++++++++++')

#也可以是一个字典格式的
s3 = Series({1:['kkk','bbb','eeeee'],2:'3333','23':'sisi'})
print(s3)
#如果没有这个key，就会赋值nan
s4 = Series(s3,index=[8,1,10])
print(s4)
print(s4.keys())
print(s4.isnull())