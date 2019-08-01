import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.path_config import mxt_account_path,used_path


#本文件用于控制读取和写入创建的账号
global mark,mxt_account_path,account,phone_number

def get_account_phonenumber():
    #print(temp)
    f = open(mxt_account_path,'r')
    temp = f.readlines()
    mark = int(temp[-1]) +1
    account = temp[0].strip('\n') +str(mark)
    #print(account)
    phone_number = str(int(temp[1])  + mark)
    #print(phone_number)

    return account,phone_number,mark
    f.close()


def write_account_phonenumber(account,phone_number,mark):
    f = open(mxt_account_path,'a')

    f.write(account+'\n')
    f.write(phone_number+'\n')
    f.write(str(mark) + '\n')
    f.close()
#print(get_account_phonenumber())

def get_reco_prepare_info():
    #为recommend模块获取用户名和电话

    f = open(mxt_account_path,'r',encoding='utf-8')
    temp = f.readlines()
    account = temp[-3].strip('\n')
    phone_number = temp[-2].strip('\n')
    return account,phone_number
    f.close()

#print(get_reco_prepare_info())