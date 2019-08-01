# 采集任务管理
import http.client
import importlib, sys, time, requests, xlrd
importlib.reload(sys)
headers = {
    'token': "7l/w+rMSKEEAjpYmARkyNJU0Kr8=",
    'cache-control': "no-cache",
    'postman-token': "9480ad8c-9ba5-47f5-6ba5-aeb0b9872753"
}

Testdata = xlrd.open_workbook('C:\\Users\\liuh\\Desktop\\test_t.xlsx', 'r')
table = Testdata.sheets()[2]
for i in range(1, table.nrows):
    path = table.cell(i, 7).value
    param = table.cell(i, 8).value
    ip = 'http://192.168.144.33:8108'
    url = ip+path+param
    result = requests.get(url,headers=headers)
    print(result)
    print(result.content.decode('utf-8'))



