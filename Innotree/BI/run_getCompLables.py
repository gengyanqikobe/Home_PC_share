

from Innotree.BI.get_cookie import get_Cookie
from Innotree.BI.getCompLabelsPresto import compLabels

def run_getLable():

    cookie = get_Cookie()               #获得cookie
    #print(cookie)

    f = open('compid_all.txt','r',encoding='utf-8')         #读待测的公司id
    ncids = f.readlines()
    #print(ncids)
    f.close()

    data = []                           #创建空列表存放结果
    for ncid in ncids:
        ncid = ncid.strip('\n')
        data.append(compLabels(cookie,ncid))
    print(data)

    f = open('result.txt','w',encoding='utf-8')     #将结果写入到文件
    for i in data:
    #print(i)
        f.write(str(i) + '\n')

    f.close()

run_getLable()