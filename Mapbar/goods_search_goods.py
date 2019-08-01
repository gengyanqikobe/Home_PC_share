# coding: utf-8
import importlib,sys,time,requests,xlrd
importlib.reload(sys)
#token = user.gettoken.gettoken()
Testdata = xlrd.open_workbook('C:\\Users\gengyq\\Desktop\\yixincase.xlsx', 'r')
table = Testdata.sheets()[3]  # 选择第一个sheet
for i in range(1, table.nrows):  # 一共多少行参数，后边这个值就写多少
    time.sleep(0.5)
    path = table.cell(i, 7).value
    param = table.cell(i, 8).value  # 读取参数，cell的第一个数是行，第二个是列
    print(param)
    url = 'http://192.168.85.70:7777' + path
    headers = {'token': token, 'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, data=param.encode(encoding='utf-8'))
    with open('F:\\python_param\\yixin\\goods_result.csv', 'a') as f:

        f.write('\n')
        f.write(str(r.text))
        f.write('\n')
