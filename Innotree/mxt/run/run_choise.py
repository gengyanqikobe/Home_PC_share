
#通过输入数字判断需要自动化的种类
import os
import sys
sys.path.append('C:\\Users\\hasee\\PycharmProjects')


tar = input("请输入数字选择需要自动化的项目：\n '1'注册贸信通账号 \n '2'分步注册基本认证信息 \n '3' 一步完成基本认证信息(到可以进行推荐认证)\n '4' 一步完成推荐信息认证\n")
if tar == '1':
    os.system("python run_register.py")
elif tar == '2':
    os.system("python run_base_ident_part.py")
elif tar == '3':
    os.system("python run_base_ident_comp.py")
elif tar =='4':
    os.system("python run_base_ident_comp.py")
    os.system("python run_recommend.py")
else:
    print("输入有误")