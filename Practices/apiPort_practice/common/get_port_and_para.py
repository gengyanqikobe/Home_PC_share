#


#用来从excel中获取接口名称和参数名称，sheet页默认为port_and_parameter

import xlrd

def get_port_and_para():

    f = xlrd.open_workbook('C:\\Users\\hasee\\PycharmProjects\Practices\\apiPort_practice\\testFile\case\park.xls')

    table = f.sheet_by_name('port_and_parameter')

    nrows = table.nrows
    ncols = table.ncols

    dict_port_and_para = {}

    for i in range(nrows):
        print(i)
        dict_port_and_para.update({table.cell_value(i,0):table.cell_value(i,1)})

    print(dict_port_and_para)

    return dict_port_and_para

get_port_and_para()