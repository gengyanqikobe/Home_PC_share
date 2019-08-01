import xlrd
import random
from xlutils.copy import copy
import xlwt
from xlwt import *
#EXCEL的读取+++++++++++++++++++++++++++++++++++++++++++
#Book = xlrd.open_workbook("D:/test3.xls",'r')
#print(Book.nsheets)#获取sheet数量

#print(Book.sheets())#获取sheet内容

#print(Book.sheet_names())#获取sheet名称

#sheet = Book.sheets()[1]#三种都是获取Book中的sheet
#sheet = Book.sheet_by_index(0)
#sheet = Book.sheet_by_name(u'testsheet')
#print(sheet)

#print(sheet.ncols,sheet.nrows,sheet.name)#获取表中的列数，行数，名字

#print(sheet.row(0),sheet.row_values(1),sheet.col(0),sheet.col_values(0))#获取某行，某行值列表，某列，某列值列表：

#print(sheet.cell(0,0),sheet.cell_value(0,0),sheet.cell(0,0).value)#获取单元格的值：

#EXCEL的写入++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Book1 = Workbook()
sheet = Book1.add_sheet('测试')
sheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.baidu.com";"baidu")')) #输出 "baidu

Book1.save('D:/test_t.xls')       #创建excel，并且保存，需要引入from xlwt import *
'''

#xlutils++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#from xlutils.copy import copy

Book = xlrd.open_workbook('D:/test3.xls')
sheet_read = Book.sheets()[1]
max_row = sheet_read.nrows
max_col = sheet_read.ncols#需要通过原Book取到行数和列数
#print(max_col,max_row)

new_Book = copy(Book)#复制，创建一个拷贝Book
new_sheet = new_Book.get_sheet(1)#只能用get_sheet，不能用sheets()[0],通过get_sheet()获取的sheet有write()方法
for i in range(0,max_row):#行数
    #print('i:',i)
    for j in range(0,max_col-1):#因为下面用到两个参数运行加法，所以列数减一
        #print('j:',j)
        sum =sheet_read.cell_value(i,j)+sheet_read.cell_value(i,j+1)#进行运算的时候，需要用原Book
        new_sheet.write(i,j+2,sum)
new_Book.save('D:/test3.xls')




