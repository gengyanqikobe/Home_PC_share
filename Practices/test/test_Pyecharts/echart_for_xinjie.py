

#xaxis_interval=0强制每个x轴名称都显示

from pyecharts import Bar


list_x = ['官网','PAAS','BI','知信通','园区','信通院','城市产业服务平台','泰达','金控（华菁/city）']
#list_x = [1,2,3,4,5,6,7,8,9]

list_y = [1,2,3,4,5,6,7,8,9]


bar1 = Bar(title='统计',width=1000)
bar1.add("这是统计",list_x,list_y,is_xaxislabel_align=True,xaxis_name_size =5,xaxis_interval=0,is_label_show=True)
bar1.render('forxinjie.html')