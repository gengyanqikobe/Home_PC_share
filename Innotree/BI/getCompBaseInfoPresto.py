



#BI 基本信息接口
#用于判断接口返回值的完整性

from Innotree.BI.get_cookie import get_Cookie
import requests
import json




def Baseinfo(cookie,ncid):

    url = 'http://10.64.6.35/bi/work/datasearch/getCompBaseInfoPresto.do?'
    #print(cookie)
    cookies = {
        'Cookie':cookie
    }
    par = {
        'ncid':ncid
    }

    response = requests.get(url,params= par,headers= cookies)
    #print(response.text)
    #print(response.status_code)

    dict_response = json.loads(response.content)

    list_code =[]                                                      #字典形式存储记录，0代表值为空，1代表有值


    if response.status_code != 200:             #判断接口是否正常访问
        print("接口访问出错，接口返回%d"%response.status_code)
    else:

        try:
            corp_name = dict_response['data']['compBaseInfo']['comp_full_name']     #列表第一项为公司名称
        except Exception as e:
            list_code.append("无名称公司")
        else:
            list_code.append(corp_name)


        try:
            com_web = dict_response['data']['compBaseInfo']['comp_web']         #进行第一项判断，是否有网址
        except Exception as e:
            list_code.append(0)
        else:

            if com_web == ''or com_web =='-' or com_web == '--':
                list_code.append(0)
            else:
                list_code.append(1)


        try:
            com_logo = dict_response['data']['compBaseInfo']['comp_logo']       #第二项判断，是否有公司logo
        except Exception as e:
            list_code.append(0)
        else:

            if com_logo == ''or com_logo == '-'or com_logo =='--':
                list_code.append(0)
            else:
                list_code.append(1)

        try:
            comp_introduction = dict_response['data']['compBaseInfo']['comp_introduction']        #第三项公司介绍
        except Exception as e:
            list_code.append(0)
        else:

            if comp_introduction == ''or comp_introduction == '-'or comp_introduction =='--':
                list_code.append(0)
            else:
                list_code.append(1)


        try:
            comp_address = dict_response['data']['compBaseInfo']['comp_address']       #第四项判断，公司地址
        except Exception as e:
            list_code.append(0)
        else:

            if comp_address == ''or comp_address == '-'or comp_address =='--':
                list_code.append(0)
            else:
                list_code.append(1)




    #print(list_code)
    return list_code





#Baseinfo('16157079184146609155')