


#关于xlutils的练习和使用

#当有需要追加的内容时，用这个

#https://www.cnblogs.com/zhenwei66/p/8406201.html

import xlrd
#from xlutils.copy import copy
from xlutils import copy

file =  xlrd.open_workbook('员工姓名手册.xls')

#需要在xlrd状态下获得sheet
#需要再xlrd状态下获得nrows和ncols等信息
table1 = file.sheet_by_name('frist')
nrows = table1.nrows
ncols = table1.ncols

#将xlrd状态转为xlwt对象
copy_file = copy.copy(file)

#在xlwt下需要用get_sheet，不能用sheet_by_name
table = copy_file.get_sheet(0)
print(table.name)



for i in range(nrows):
    for j in range(ncols):
        # if table.cell_value(i,j) == '李傻静4':
        #     table.write(i,j+1,33)
        table.write(i,j,33)

copy_file.save('员工姓名手册.xls')

table.write(4,1,44)

copy_file.save('员工姓名手册.xls')