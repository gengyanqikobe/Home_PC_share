
#练习多线程使用
import threading

from Innotree.BI.get_cookie import get_Cookie
from Practices.test.test_treading.getCompLabelsPresto import compLabels


def creat_ncid_data(ncids_total_numbers,thread_numbers,filename):        #输入ncid总条数和线程数,以及待测文件

    cookie = get_Cookie()               #获得cookie
    #print(cookie)

    f = open(filename,'r',encoding='utf-8')         #读待测的公司id
    ncids = f.readlines()
    #print(ncids)
    f.close()

    each_ncids_number = int(ncids_total_numbers/thread_numbers)
    each_list_ncid =[]
    total_ncids = []
    j = 0
    for i in range(thread_numbers):
        for m in range(each_ncids_number):
            each_list_ncid.append(ncids[j].strip('\n'))
            j = j + 1


        total_ncids.append(each_list_ncid)
        each_list_ncid = []
    #print(total_ncids)
    return total_ncids,cookie

def run_getLable(total_ncids,cookie):
    data = []                           #创建空列表存放结果
    for ncids in total_ncids:
        #print(total_ncids)
        print(ncids)
        t_compLables = threading.Thread(target=compLabels,args=(cookie,ncids,))
        t_compLables.start()

    # print(data)
    # f = open('result.txt','w',encoding='utf-8')     #将结果写入到文件
    # for i in data:
    # #print(i)
    #     f.write(str(i) + '\n')
    #
    # f.close()


res = creat_ncid_data(1000,20,'compid_all.txt')          #输入ncid总条数和线程数
print(res[0],res[1])
run_getLable(res[0],res[1])



