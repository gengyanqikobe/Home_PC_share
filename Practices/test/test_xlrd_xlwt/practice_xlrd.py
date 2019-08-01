


#用来进行xlrd练习
#总结，可以成功读到内容，但是想在已经有的xls文件上追加，直接用xlwt不行，这样会另外生成一个文件

import xlrd,xlwt

file = xlrd.open_workbook('员工姓名手册.xls')

#根据表名找到对应的sheet页
table = file.sheet_by_name('frist')

#拿到行数和列数
nrows = table.nrows
ncols = table.ncols
print(nrows,ncols)

#
file2  = xlwt.Workbook()
table2 = file2.add_sheet('frist',cell_overwrite_ok=True)



for i in range(nrows):
    for j in range(ncols):
        #print(table.cell_value(i,j))
        if table.cell_value(i,j) == '李傻静7':
            table2.write(i,j+1,30)

file2.save('员工花名手册.xls')



