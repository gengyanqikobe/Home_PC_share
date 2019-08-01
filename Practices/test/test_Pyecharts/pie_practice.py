from pyecharts import Pie

from Practices.test.test_Pyecharts.block import block

data = block(10,'fail.txt')
value = []
attr = []
for item in data[0]:
    temp = str(item)

    attr.append(temp)
    #print(type(temp),item)
print(len(attr),attr)

value = data[1]
print("value is",len(value),value)
#
# attr = str(data[0])

# attr = ['[1]','[2]','[3]','[4]']
# value = [1,2,3,4]

pie = Pie('\n\n\n标签接口数据缺失率饼状图',title_pos='right')

pie.add('',attr,value,is_label_show=True,label_pos='right')

pie.render('pie.html')