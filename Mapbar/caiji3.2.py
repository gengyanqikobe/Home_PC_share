import http.client
import json
import urllib.request
from urllib import request,parse
import requests

global null
null = ''

# 采集3.2任务下发接口


headers = {
    'cache-control': "no-cache",
    'postman-token': "85417d3e-83bc-0338-dd55-a33be84a6e8d"
}

'''
print('采集3.2任务下发接口:')
conn = http.client.HTTPConnection("192.168.0.175:9091")

times = int(input("请输入下发任务个数："))

f = open('caiji3.2.txt','r')
n = f.read()
f.close()


i = 0
while i < times:

    jobName = '测试'+ n
    i = i + 1
    temp = int(n) + 1  
    n = str(temp)

    payload ="{\"jobName\":\""+jobName+"\",\"timeType\":\"3\",\"beginDate\":\"2017-07-10\",\"beginTime\":\"10:02:01:328\",\"expDate\":\"2017-10-01\",\"downId\":[\"guid1\",\"guid2\"],\"idType\":\"1\"}"
    payload = payload.encode('utf-8')
    #print(payload)    #转码后的payload，是bytes   
    #print('payload is ',type(payload))


    conn.request("POST", "/job/add", payload, headers)

    res = conn.getresponse()
    data = res.read()
    #print(data)
    #print(data.decode("utf-8"))

    data = data.decode('utf-8') ##从bytes格式到str需要decode
    #print(data)
    result = eval(data)  #把str转成字典，eval
    #print(result)
    #print(type(result))
    #print(result.keys())
    key = result.keys()
    #print(type(key))
    for aa in key:
        if aa == 'resultCode':
            if result[aa] == 200:
                print('任务下发第%s次：pass'%(i))
            else: print('任务下发第%s次：no pass'%(i))


f = open('caiji3.2.txt','w')
f.write(n)
f.close()

print('+++++++++++++++++++++++++++++++++++++++++++++++')
'''
'''
#采集3.2运行任务接口
print('采集3.2运行任务接口:')

conn1 = http.client.HTTPConnection("192.168.0.175:9091")
conn1.request("GET", "/job/0?page_number=1&page_size=10", headers=headers)
job_save ='' #初始化
#print(type(job_save))
res1 = conn1.getresponse()
data1 = res1.read()

#print(data1.decode("utf-8"))
yx_str_result = eval(data1)
yx_key = yx_str_result.keys()
#print(yx_key)
for aa in yx_key:
    if aa =='resultCode':
        if yx_str_result[aa] == 200:
            print('pass')
        else: print('no pass')
    if aa =='data':
        yx_str_result1 = yx_str_result[aa]
        for bb in yx_str_result1:
            if bb =='data':
                #print(yx_str_result1[bb])
                if yx_str_result1[bb] == []:#用None什么的不可以好像
                    print('no data')
                    continue
                for cc in yx_str_result1[bb]: #选出list表中的每一项
                    dd = cc
                    for ee in dd:
                        if ee == 'jobId':
                                #print(type(dd[ee]))
                                job_save = job_save +dd[ee] +'\n'  #把得到的jobid都写进字符串里
                                #print(job_save)
f_savejob = open('caiji3.2jobId.txt','w')  #将得到的jobid写进文件中
f_savejob.write(job_save)
f_savejob.close()
print('+++++++++++++++++++++++++++++++++++++++++++++++')
'''
'''
#采集3.2条件查询接口
print('采集3.2条件查询接口:')
query = http.client.HTTPConnection("192.168.0.175:9091")

f_query = open('caiji3.2jobId.txt')
query_jobid= f_query.readlines() #以list格式读出来
#print(query_jobid)
#print(type(query_jobid))
f_query.close()
#print(query_jobid[0])
for jobid in query_jobid:
    jobid = jobid[0:-1]  #去除掉最后的回车
    if jobid =='':
        continue
    else:
        #print(jobid)
        break


#jobid = query_jobid[0]

#print(jobid)
#print(type(jobid))   
query.request("GET", "/job/0/"+jobid+"?page_number=1&page_size=2", headers=headers)#双引号弄参数化
query_res = query.getresponse()
query_data = query_res.read()
#print(query_data.decode('utf-8'))

query_result = eval(query_data)
#print(query_result)
#print(type(query_result))
query_key = query_result.keys()
#print(query_key)

for aa in query_key:
    if aa == 'data':
        query_result1 = query_result[aa]
        #print(query_result1)
        for cc in query_result1:
            if cc =='totalNum':
                if query_result1[cc] == 1:
                    #print(query_result1[cc])
                    print("pass")
                else :
                    print("noexist")


print('+++++++++++++++++++++++++++++++++++++++++++++++')


#采集3.2查询详情接口

print("查询详情接口:")
f_detail = open('caiji3.2jobId.txt')
detail_jobid = f_detail.readlines()
#print(detail_jobid)
f_detail.close()

for jobid in detail_jobid :
    jobid = jobid[0:-1]
    if jobid == '':
        continue
    else:
        #print(jobid)
        break
#jobid = '111'
detail = http.client.HTTPConnection("192.168.0.175:9091")
detail.request("GET","/job/query/"+jobid+"?",headers = headers)
detail_res = detail.getresponse()
detail_data = detail_res.read()
#print(detail_data.decode('utf-8'))     #两种办法解决eval将str转成字典的方法，一个是用loads，一个是用全局变量null=''
tem_data =detail_data.decode('utf-8')

detail_result = json.loads(tem_data)
#detail_result = eval(detail_data)
#print(detail_result)
#print(type(detail_result))
for aa in detail_result:
    if aa =='resultCode':
        if detail_result[aa] ==200:
            print('pass')
        else:
            print('nopass')


print('+++++++++++++++++++++++++++++++++++++++++++++++')

=
#采集3.2删除任务

def caijidelete(jobid,control_print):
    if control_print == 1:
        print('采集3.2删除任务:')
        control_print = control_print +1

    #print(control_print)
    delete = http.client.HTTPConnection("192.168.0.175:9091")
    delete.request("POST","/job/del/"+jobid+"",headers = headers)
    delete_res = delete.getresponse()
    delete_data = delete_res.read()

    #print(delete_data.decode('utf-8'))
    delete_result = eval(delete_data)
    if delete_result['resultCode'] == 200:
        if delete_result['message'] == '':
            caijidelete(jobid,control_print)
        elif delete_result['message'] == 'jobId ready del':
            print('pass')
    else:
        print('nopass')

caijidelete(jobid,1)


print('+++++++++++++++++++++++++++++++++++++++++++++++')


# 采集3.2查询当前appkey

def caijiappkey():
    print('采集3.2查询当前appkey:')
    url = "http://192.168.0.175:9091/appkey?page_number=1&page_size=1"
    data = urllib.request.urlopen(url).read()
    # print(data.decode('utf-8'))

    result = eval(data)
    # print(result)
    if result['resultCode'] == 200:
        print('pass')
    else:
        print('nopass')


caijiappkey()

print('+++++++++++++++++++++++++++++++++++++++++++++++')


#采集3.2历史统计接口
def historyCount(jobid):
    print("采集3.2历史统计接口:")
    #print(jobid)
    url ="http://192.168.0.175:9091/job/HistoryCountInfo/"+jobid+"?page_number=1&page_size=4"
    data = urllib.request.urlopen(url).read()
    #print(data.decode('utf-8'))
    result = eval(data)
    if result['resultCode'] == 200:
        print('pass')
    else:
        print('nopass')

historyCount(jobid)

print('+++++++++++++++++++++++++++++++++++++++++++++++')

'''


#采集3.2同步appkey接口
def addappkey():
    print('采集3.2同步appkey接口:')

    url = "http://192.168.0.175:9092/add/appkey"

    payload = '{"app_key":"key11111","app_type":"1","app_name":"appkeyName","operate_plat":"1","description":"看看"}'
    print(type(payload))
    data = payload.encode('utf-8')
    print(type(data))
    response = requests.request("POST", url, data=data)
    #print(response.text)
    result = eval(response.text)
    #print(result)
    if result['code'] == '200':
        print('pass')
    else:
        print('nopass')



addappkey()




















