



from pandas import Series,DataFrame
import pandas as pd


data = {'name':['xiaohong','xiaoli','xiaowang'],'age':[22,34,33],'sex':['M','W','M']}

f1 = DataFrame(data)
print(f1)

#可以更换列column的位置
print('================================================')
f2 = DataFrame(data,columns=['name','sex','age'])
print(f2)

print('==========================================')
#可以构造一个seriex，增加到dataframe中，因为每一列都是一个series
s1 = Series(['是','否','是'])

f2['single'] = s1

print(f2)

#精准修改
print(111111111111111111111111111111111111111111111)
f2['name'][1] = 'xiaolan'

print(f2)
print('=====================================')
print(f2.to_html)