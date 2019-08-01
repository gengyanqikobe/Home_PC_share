# 采集任务管理
import http.client
import importlib, sys, time, requests, xlrd,urllib

importlib.reload(sys)

Testdata = xlrd.open_workbook('C:\\Users\gengyq\Desktop\采集监控（任务管理）接口测试用例2017-10-31.xlsx', 'r')

for j in range (2,4):
    table = Testdata.sheets()[j]
    #table = Testdata.sheets()[2]
    #print(j)
    for i in range(1, table.nrows):
        name = table.cell(i, 1).value
        target = table.cell(i, 3).value
        ex_value = table.cell(i,5).value

        path = table.cell(i, 7).value
        # print(path)
        param = table.cell(i, 8).value
        # print(type(param))
        # print(param)
        headers = {"token": "7l/w+rMSKEEAjpYmARkyNJU0Kr8="
                   }

        ip = 'http://192.168.144.33:8108'
        url = ip + path + param
        print(url)

        res = requests.get(url, headers=headers)
        print(res.text)
        data = res.text
        # print(type(data))
        # print(data)

        f = open('C:\\Users\gengyq\Desktop\caijiguanli.txt', 'a')
        f.write('接口名：' +name + '  ' + '目标：'+target + '   '+ '预期值：'+ ex_value + '\n\n')
        f.write(data)
        f.write('\n\n\n')
        f.close()





