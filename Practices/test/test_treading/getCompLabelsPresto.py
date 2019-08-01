

#BI系统公司详情-基本信息-标签接口
 #"输出格式说明:[{公司id:公司名称 好数据百分比},[好数据百分比，坏数据百分比，数据完整性],[{标签1：数量},{标签2：数量}....]]"



#练习多线程使用

import requests
import json
from Innotree.BI.get_cookie import get_Cookie
import time



def compLabels(cookie,ncids):
    cookie = cookie
    global corp_name
    for ncid in ncids:

        results = []
        corp_name= '公司无名称'
        #print(ncid)
        dict_ncid ={}
        dict_rat_good ={}
        dict_bad ={}
        corp_result =[]
        result = []

        cookies ={
            'Cookie':cookie
        }
        url = 'http://10.64.6.35/bi/work/datasearch/getCompLabelsPresto.do?'
        par = {
            'ncid':ncid
        }

        response = requests.get(url,params=par,headers= cookies)
        #print(response.text)
        dict_res = json.loads(response.content)
        dict_data = dict_res['data']
        #print(dict_data)

        count_bad =0
        count_total = 0
        list_bad = []
        tag_total = []
        list_rat = ['基本信息-标签接口']
        tag = {}

        for i in dict_data:
            #print(i)
            count_total = count_total +1    #标签总数加一
            if dict_data[i] ==[] or dict_data[i] == 'null'or dict_data[i] == None or dict_data[i] == '':
                #print("dict_data[i] is:",dict_data[i])
                count_bad = count_bad + 1   #坏标签数加一
                list_bad.append(i)          #把坏标签放入列表
            else:
                #print("dict_data[i] is:",dict_data[i])

                count_tag = len(dict_data[i])



                tag = {i:count_tag}  #每一个tag的数量
                #print(tag)
                tag_total.append(tag)           #将所有tag和他的数量信息放入tag集合表里面
                #print(tag_total)

        try:

            corp_name = dict_data['businessScopeTag'][0]['comp_full_name']#获取公司名称
            #print(corp_name)
        except Exception as e:
            pass




        rat_good = round((count_total - count_bad)/count_total *100 ,2)#计算合格数据概率
        rat_bad = round(100 - rat_good,2)
        str_rat_good = str(rat_good)+'%'    #将值转为字符串格式

        #print(rat_good,str_rat_good)
        str_rat_bad = str(rat_bad)+'%'
        list_rat.append(str_rat_bad)
        list_rat.append(str_rat_good)
        rat_whole = round(count_total/count_total,4)*100
        str_rat_whole = str(rat_whole)+'%'
        list_rat.append(str_rat_whole)                          #分别把好数据，坏数据，完整性放入列表



        dict_ncid = {ncid:corp_name + ' '+ str_rat_good}             #组成id：公司名字+好数据的字典

        result.append(dict_ncid)
        result.append(list_rat)
        result.append(tag_total)

        # g = open('fail.txt','a',encoding='utf-8')
        # g.write(str_rat_bad+'\n')
        # g.close()
        #results.append(result)
        f = open('result.txt','a',encoding='utf-8')
        f.write(str(result) + '\n')
        f.close()


