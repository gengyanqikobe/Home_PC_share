
#本文档用于学习和练习xlwt的使用

import xlwt,xlrd

#创建一个文档
new_excel = xlwt.Workbook()

#新建一个newsheet
table = new_excel.add_sheet('frist',cell_overwrite_ok=True) #加上这个重复写入状态为True，重复操作单元格的时候就不报错了


#写入数据,行，列，内容
table.write(0,0,'姓名')
table.write(0,1,'年龄')

for i in range(1,10):
    table.write(i,0,'李傻静'+str(i))
    table.write(i,1,20)


new_excel.save('员工姓名手册.xls')