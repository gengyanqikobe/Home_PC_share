

#判断标准：1.尽可能在一家店买到最多的书
#           2.这本书在这家书店尽可能便宜,排名靠前的打分低，分越低越值得购买





import xlrd
import xlutils

from pyecharts.charts import Bar

import webbrowser
from pandas import DataFrame
import pandas


f = xlrd.open_workbook('kongfz_price.xls')

table = f.sheet_by_name('book_price')

nrows =table.nrows
ncols =table.ncols
#print(nrows,ncols)

#存储店名和数量
dict_shop_count = {}
#存储店名和书名
dict_shop_bookname = {}

dict_sp_co_show  = {}
dict_shop_bookname_show = {}
dict_sp_score_price = {}
dict_sp_score_price_show = {}
dict_sp_score_avg_price_show = {}
n = 0
for i in range(1,nrows):
    n = 0
    temp_bookename = ''
    temp_score = 0
    for j in range(1,ncols):
        #print("i,j",i,j)
        if table.cell_value(i,j) != '' :
            #print(table.cell_value(i,j))
            n += 1
            temp_bookename = temp_bookename + ' '+table.cell_value(0,j)     #临时书名
            #print(str(table.cell_value(i,j)).split(',')[0])
            temp_score = int(str(table.cell_value(i,j)).split(',')[0]) + temp_score     #对分数，价格进行切割

    dict_shop_count.update({table.cell_value(i,0):n})
    dict_shop_bookname.update({table.cell_value(i,0):temp_bookename})
    dict_sp_score_price.update({table.cell_value(i,0):temp_score})

    count = 0
#print(dict_sp_score_price)
#print(dict_shop_count)
#print(dict_shop_bookname)


#筛选单一店铺可以买到书的数量
for key in dict_shop_count.keys():
    #print(dict_shop_count[key])
    if dict_shop_count[key] >5:
        dict_sp_co_show.update({key:dict_shop_count[key]})
        dict_shop_bookname_show.update({key:dict_shop_bookname[key]})
#print(dict_sp_co_show)
#print(dict_shop_bookname_show)

#构造得分字典
for key in dict_sp_co_show.keys():
    dict_sp_score_price_show.update({key:dict_sp_score_price[key]})
#print(dict_sp_score_price_show)

#构造平均得分字典,分数越低越值得购买
for key in dict_sp_co_show.keys():
    dict_sp_score_avg_price_show.update({key:round(dict_sp_score_price_show[key]/dict_sp_co_show[key],2)})
#print(dict_sp_score_avg_price_show)



#html中换行用<br>
str_dict_shop_bookname = ''
for key in dict_shop_bookname_show.keys():
    str_dict_shop_bookname = str_dict_shop_bookname + key + ':<br>' +dict_shop_bookname_show[key] + '<br><br>'
#print(str_dict_shop_bookname)
'''
#构造一个html文件
f_html = open('shopname_bookname.html','w')
message ="""
<html>
<head></head>
<body>

<a href='http://localhost:63342/PycharmProjects/Practices/kongfz/shop_count.html'>
<br>
<u>图书数量与购买建议图表</u>
<br>
<br>
</a>
<t>%s</t>
</body>
</html>"""%(str_dict_shop_bookname)
f_html.write(message)

f_html.close()
'''


#横坐标店名，纵坐标书的数量
list_x = []
list_value = []
list_value_avg_score = []
for x in dict_sp_co_show.keys():
    list_x.append(x)
    list_value.append(dict_sp_co_show[x])
    list_value_avg_score.append(dict_sp_score_avg_price_show[x])

#print(list_x,list_value)



#书店数量柱状图
bar_shop_count = Bar('数量\n代表这家店内同\n时可买的书籍\n\n级别\n数值越低\n低越值得购买',width='100%',height=600,subtitle_color='red',page_title="孔夫子价格筛选",title_text_size=15,renderer='canvas')
bar_shop_count.add('图书数量',list_x,list_value,is_label_show=True,is_more_utils=False,is_datazoom_show=False,xaxis_interval=0,is_xaxislabel_align=True)
bar_shop_count.add('推荐级别',list_x,list_value_avg_score,is_more_utils=True,is_label_show=True,legend_text_color='blue',is_datazoom_show=False,xaxis_interval=0,is_xaxislabel_align=True,xaxis_name='书店',xaxis_name_pos='end',yaxis_name_pos='end',yaxis_name='数量|分数')
bar_shop_count.render('shop_count.html')






#==========构建一个表格

#print(dict_shop_bookname_show)
list_bookname = []
list_shopname = []
list_score = []
list_count = []

for key in dict_shop_bookname_show.keys():
    list_shopname.append(key)
    list_bookname.append(dict_shop_bookname_show[key])

for key in list_shopname:
    list_score.append(dict_sp_score_avg_price_show[key])

for key in list_shopname:
    list_count.append(dict_shop_count[key])
#print(list_shopname,list_bookname)
#可以调整显示的宽度，这样就不会出现。。。的省略号了
pandas.set_option('display.max_colwidth',500)


index = list_shopname
df = DataFrame(index=index)
df['推荐级别'] = list_score
df['图书数量'] = list_count
df['书名'] = list_bookname
print(df)


#写入‘shop_count.html
f_html = open('shop_count.html','a',encoding='utf-8')
message ="""
<html>
<head>
<style>
table,tr{
text-align:center!important;
margin:auto;
}
</style>
</head>
<body>
</body>
</html>"""
f_html.write(message)
f_html.write(df.to_html(classes='df'))

f_html.close()
