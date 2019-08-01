#给孙喜下发任务用
import http.client

conn = http.client.HTTPConnection("martc.mapbar.com")#smartc.mapbar.com

times = int(input("请输入执行次数："))
j = int(input("请输入开始分钟数："))
i = 0

while i < times:
    jobName = '取任务test' + str(i)
    if j< 10:
        beginTime_mintus ='16:' + '0' +str(j) + ':55:328'
    elif j>59:
        print("分钟数不能超过60")
        break
    else:
        beginTime_mintus = '16:' + str(j) + ':55:328'
    
 
    print(beginTime_mintus)
    i = i + 1
    j = j + 2

    payload ="{\"jobName\":\""+jobName+"\",\"timeType\":\"3\",\"beginDate\":\"2017-11-03\",\"beginTime\":\""+beginTime_mintus+"\",\"expDate\":\"2017-11-25\",\"downId\":[\"608A35C6-F646-7FDB-F686-9765162F6A4A\"],\"idType\":\"1\",\"token\":\"tikD0P2jnHWs8EQsPG84PqAtnLg%3D\",\"_rid\":\"0.6409085320100396\"}"
    headers = {
    'cache-control': "no-cache",
    'postman-token': "85417d3e-83bc-0338-dd55-a33be84a6e8d"
    }
    payload = payload.encode('utf-8')

    conn.request("POST", "/serviceapi/job/add", payload, headers)#/serviceapi/job/add

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    



    



