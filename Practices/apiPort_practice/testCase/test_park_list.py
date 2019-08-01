
#将unittest和excel接口自动化测试结合


import unittest
from xlutils.copy import copy

import xlrd
import requests
from Practices.apiPort_practice.common.get_port_and_para import get_port_and_para

class Park_List(unittest.TestCase):
    def park_list(self):


        f = xlrd.open_workbook('C:\\Users\\hasee\\PycharmProjects\Practices\\apiPort_practice\\testFile\case\park.xls')
        #接收接口名称和参数名称
        dict_port_and_para = get_port_and_para()
        print(dict_port_and_para)

        for portname in dict_port_and_para.keys():

            table = f.sheet_by_name(portname)

            list_sheets = f._sheet_names                #获取到case里面所有的sheet名称
            #print(list_sheets)
            f2_sheet_number = list_sheets.index(portname)   #根据port名字，确定这一页的索引位置，并赋值给复制后的excel
            print(f2_sheet_number)
            #print(f._sheet_names)


            nrows = table.nrows
            ncols = table.ncols

            f2 = copy(f)
            table2 = f2.get_sheet(f2_sheet_number)

            str_par = dict_port_and_para[portname]
            list_pra = str_par.split(',')               #字符串转成列表参数

            dict_pra_temp = {}
            for i in  list_pra:
                print(i)

            #找到参数所在列
            for i in range(1):
                for j in range(ncols):
                    if table.cell_value(i,j) in list_pra:
                        dict_pra_temp.update({table.cell_value(i,j):j})     #将参数名称和它所在的列号存在一个字典里面，如{id，5}
                        #print(dict_pra_temp)


            for i in range(1,nrows):
                dict_para = {}                                              #最后要用到的参数字典

                #print(dict_pra_temp.keys())
                for key in  dict_pra_temp.keys():
                    cell = table.cell(i,dict_pra_temp[key])
                    #print(cell.ctype)                                       #查看value的类型，1为str，2为float或者int
                    if cell.ctype ==2 and cell.value % 1 ==0:               #判断是否为数字，如果是的话下面就保存为int

                        para_value = int(table.cell_value(i,dict_pra_temp[key]))
                    #print(key,para_value,type(para_value))
                    else:
                        para_value = table.cell_value(i,dict_pra_temp[key])
                    dict_para.update({key:para_value})


                    #print(dict_para)
                #print(dict_para)
                cell_code = table.cell(i,5)
                if cell_code.ctype ==2 and cell_code.value % 1 == 0:
                    code = int(table.cell_value(i,5))

                desc = table.cell_value(i,6)


                response = requests.post(url= 'http://test-api.innotree.com/park/service/park/list',data = dict_para)
                #print(response.)
                print(response.text)
                #print(type(response.text))
                dict_response = eval(response.text)
                #print(code)

                try:
                    res_code = dict_response['code']
                    #print(res_code)
                except Exception as e:
                    print('接口没有返回code')
                else:
                    try:

                        self.assertEqual(res_code,code,"返回值与预期不符")
                    except Exception as e:
                        #print(e)
                        table2.write(i,7,"fail")
                        f2.save('C:\\Users\\hasee\\PycharmProjects\Practices\\apiPort_practice\\testFile\case\park.xls')
                    else:
                        table2.write(i,7,'pass')
                        f2.save('C:\\Users\\hasee\\PycharmProjects\Practices\\apiPort_practice\\testFile\case\park.xls')