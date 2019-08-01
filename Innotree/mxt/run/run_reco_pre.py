import sys

sys.path.append("C:\\Users\\hasee\\PycharmProjects")

from Innotree.mxt.function.recommend_prepare import reco
account = input("请输入企业名称：")
phonenumber = input("请输入企业电话：")

#用于完成了基本认证缴费后的用户

reco(account,phonenumber)