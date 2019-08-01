from xlrd import open_workbook
import os

def get_xls(xls_name,sheet_name):
    case = []
    proDir = os.path.split(os.path.realpath(__file__))[0]
    xls_path = os.path.join(proDir,xls_name)
    file = open_workbook(xls_path)
    print(file.nsheets)

    sheet = file.sheet_by_name(sheet_name)
    print(sheet.nrows,sheet.name,sheet.ncols)

    nrows = sheet.nrows
    for i in range(nrows):
        #print(sheet.row_values(i))
        if sheet.row_values(i)[0] != None:
            case.append(sheet.row_values(i))
    return case



case = get_xls('personn_information.xlsx','login')
case1 = get_xls('personn_information.xlsx','age')
print(case,case1)