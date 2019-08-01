from pyecharts import Bar

from Practices.test.test_Pyecharts.block import block

data = block(20,'fail.txt')
print(data[0])
values = []
x = []

x = data[0]
print(x)
values = data[1]
print(values)

#x = ['一月','二月','三月','四月','五岳']

bar1 = Bar('标签接口数据缺失率\n横坐标为缺失比例，纵坐标为该比例下的数量',width=1600,height=600)
bar1.add('数据缺失',x,values,is_more_utils=True,is_label_show=True,label_pos='top')
bar1.render('bar.html')
print(bar1._page_title)