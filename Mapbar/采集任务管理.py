#采集任务管理
import http.client
import importlib,sys,time,requests,xlrd


conn = http.client.HTTPConnection("192.168.144.33:8108")
headers = {
    'token': "7l/w+rMSKEEAjpYmARkyNJU0Kr8=",
    'cache-control': "no-cache",
    'postman-token': "9480ad8c-9ba5-47f5-6ba5-aeb0b9872753"
    }

importlib.reload(sys)




#token = '7l/w+rMSKEEAjpYmARkyNJU0Kr8='
Testdata = xlrd.open_workbook('C:\\Users\gengyq\\Desktop\\采集监控（任务管理）接口测试用例2017-10-31.xlsx','r')
table = Testdata.sheets()[2]
for i in range(1,table.nrows):
    name = table.cell(i,1).value
    target = table.cell(i,3).value
    path = table.cell(i,7).value
    #print(path)
    param = table.cell(i,8).value
    #print(type(param))
    #print(param)
    url = path + str(param.encode('utf-8'))
    print(url)
    conn.request("POST",url , headers=headers)
    
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    print(data)
    f = open('C:\\Users\gengyq\\Desktop\\caijiguanli.txt','a')
    f.write(name + '  ' + target +'\n')
    
    f.write(data)
    f.write('\n\n')
    f.close()

    
    
    
