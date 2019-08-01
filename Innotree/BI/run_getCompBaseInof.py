


#获取ncid并且执行getCompBaseInfo文件,计算每一项的覆盖率并写入result_baseinfo.txt文件

from Innotree.BI.getCompBaseInfoPresto import Baseinfo
from Innotree.BI.get_cookie import get_Cookie


def run_getBaseInfo(count_number):  #需要输入统计项数

    cookie = get_Cookie()               #获得cookie
    #print(cookie)

    f = open('compid_all.txt','r',encoding='utf-8')         #读待测的公司id
    ncids = f.readlines()
    #print(ncids)
    f.close()

    count = []
    rate = []
    for i in range (0,count_number):
        count.append(0)


    data = ['','输出格式为[公司名称，网址，logo，介绍，地址]','']                           #创建列表存放结果
    count_ncids = 0
    for ncid in ncids:
        count_ncids +=1
        print(count_ncids)
        ncid = ncid.strip('\n')
        temp_data = Baseinfo(cookie,ncid)
        data.append(temp_data)

        i = 1
        for i in range(1,5):            #从返回的list中取值，计数
            #print(temp_data[i],type(temp_data[i]))
            if temp_data[i] == 1:
                count[i-1] += 1
                #print(count)
            i = i +1

    #print(count)
    for i in count:                     #根据数值计算每一项的百分比
        rat = round(i/count_ncids*100,2)
        rate.append(str(rat) + '%')
    print(rate)

    #print(data)

    f = open('result_baseinfo.txt','w',encoding='utf-8')     #将结果写入到文件
    f.write(str(rate) + '\n')
    for i in data:
    #print(i)
        f.write(str(i) + '\n')

    f.close()




run_getBaseInfo(4)