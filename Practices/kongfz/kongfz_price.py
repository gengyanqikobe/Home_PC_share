
#总结，访问不通过，就加headers，好使。

#不用登录就 可以查询书

#取前30家时间太长（2小时多），效率过低，现在改为取前10家。

#注意：先整理数据再进行操作，这样可以省很多事情，不要让它一直遍历，费时间。

#!!!!str转为字典的时候，用json.loads比eval好用，我也不知道为什么，突然就就不行了,因为返回的结果孔夫子增加了个true字段，而且没有用''括起来，所以eval转换的时候出错了



import requests
import xlrd
from xlutils.copy import copy
import time
import json



#获取书名
f = xlrd.open_workbook('kongfz_price.xls')
table = f.sheet_by_name('book_price')
ncols = table.ncols
nrows = table.nrows
nrows_changed = nrows
#print(table.cell_value(100,100))

f2 = copy(f)
table2 = f2.get_sheet(0)

for i in range(1,ncols):
    #print(table.cell_value(0,i))


    key = table.cell_value(0,i)

#       'order'字段为排序方式，目前采取的是总价从低到高
    #从excel中取到书名，然后组成url
    url = 'http://search.kongfz.com/product_result/?select=0&key='+key+'&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&order=100&type=1&ajaxdata=1&_=1562552199178'
    print(url)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'acw_tc=276077a315625477114962925e891e9592d0223b09d0273f0e0267a6b6971d; kfz_uuid=215f48eaab1c63558373929c225bc140; shoppingCartSessionId=220c308ef9280b392074161f7e9a0a37; reciever_area=1006000000; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1562547716; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1562547716; token=73ad8283222604ae70e12c518e8be8bc; PHPSESSID=itqcsdsafne4u3s00hnobq8a66; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1563172093; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1563172093; kfz-tid=ff025ce0e5d2af7e5badb4a047f2c6fc',
        'Host':'search.kongfz.com',
        'Proxy-Connection':'keep-alive',
        'Referer':'http://search.kongfz.com/product_result/?select=0&key=%E9%BB%91%E7%8C%AB%E9%A6%86%E4%BA%8B%E4%BB%B6&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&order=200',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }

    time.sleep(3)
    response = requests.get(url=url,headers =headers)

    print(type(response.text))
    print(response.text)
    try:

        #dict_response = eval(response.text)
        dict_response = json.loads(response.text)
        #print(dict_response['data']['itemList'])
    except Exception as e:
        print("没有搜索到",key)
    else:
        list_response = dict_response['data']['itemList']
        #print(len(list_response))
        #print(list_response)

        #for循环遍历，寻找价格，书店名称等信息
        dict_shop_price = {}
        for item in list_response[:5]:
            print(item['price'],item['shopname'])
            if item['shopname'] in dict_shop_price.keys():
                continue
            else:
                dict_shop_price.update({item['shopname']:item['price']})
        print(dict_shop_price)


        score = 1
        #将过滤过的信息写入excel
        for key in dict_shop_price.keys():
            f3 = xlrd.open_workbook('kongfz_price.xls')
            table3 = f3.sheet_by_name('book_price')
            write_status = False

            for sp_i in range(nrows_changed):
                sp_name = table3.cell_value(sp_i,0)

                if sp_name ==key:
                    table2.write(sp_i,i,str(score) +',' + dict_shop_price[key])
                    f2.save('kongfz_price.xls')
                    write_status = True
                    continue

            if write_status ==False:
                    table2.write(nrows_changed,0,key)
                    table2.write(nrows_changed,i,str(score) +',' + dict_shop_price[key])
                    f2.save('kongfz_price.xls')
                    nrows_changed = nrows_changed +1
            score = score + 1





'''
        for item in list_response[:30]:     #取最低价格的前30家
            print(item['price'],item['shopname'])
            price = item['price']
            shopname = item['shopname']


            #print(nrows)
            #如果店已经存在，则追加内容状态为，不存在则新增店名再追加内容,
            write_status = False
            for sp_i in range(nrows_changed):
                f3 = xlrd.open_workbook('kongfz_price.xls')     #再用xlrd.open打开一次，因为上面的f不能事实刷新，获取不到最新的行数，或导致list超出范围
                table3 = f3.sheet_by_name('book_price')
                sp_name = table3.cell_value(sp_i,0)
                if shopname == sp_name :   #已经填写过就不会被覆盖
                    if table3.cell_value(sp_i,i) =='':
                        table2.write(sp_i,i,price)
                        f2.save('kongfz_price.xls')
                        write_status = True
                        continue
                    else:
                        break

            if write_status ==False:



                table2.write(nrows_changed,0,shopname)
                table2.write(nrows_changed,i,price)
                f2.save('kongfz_price.xls')
                nrows_changed = nrows_changed +1

'''