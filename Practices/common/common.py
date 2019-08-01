import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
import Practices.common.configHttp as configHttp
from Practices.readConfig import proDir

localConfigHttp = configHttp.ConfigHttp()

def get_xls(xls_name,sheet_name):
    cls = []
    #获得xls文件路径,需要引用一下
    xlsPath = os.path.join(proDir,"testFile",xls_name)
    #打开xls文件
    file = open_workbook(xlsPath)
    #获得sheet表
    sheet = file.sheet_by_name(sheet_name)
    #获得sheet里面的row
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i) != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

