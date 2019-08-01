import os
#用于完成基础信息认证，推荐认证准备状态
import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.function.recommend_prepare import reco
from Innotree.mxt.path_config import mxt_account_path


for i in range(0,3):
    #填写基础信息
    os.system("python C:\\Users\\hasee\\PycharmProjects\\Innotree\\mxt\\function\\baseid_comp.py")
    #完成基础信息认证,从刚注册完毕的
    f = open(mxt_account_path,'r')
    temp = f.readlines()
    account = temp[-3].strip('\n')
    phone_number = temp[-2]
    #corp_name = '京点星（北京）贸易有限公司'
    f.close()
    #reco(account,phone_number)
