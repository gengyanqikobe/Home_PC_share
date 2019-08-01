import os
import sys

path_dir = os.path.split(os.path.realpath(__file__))[0]
#print(path_dir)

#存储贸信通的测试账号文档mxt_account.txt
mxt_account_path = os.path.join(path_dir,'mxt_account.txt')
#autoit所生成的软件
mxt_picture_exe_path = "C:\\Users\\hasee\Documents\\mxt_tp.exe"
mxt_ppt_exe_path = "C:\\Users\\hasee\Documents\mxt_wendang.exe"

#贸信通项目中config.ini地址
mxt_config_path = os.path.join(path_dir,'config.ini')

#used文件路径
used_path = os.path.join('C:\\Users\\hasee\\PycharmProjects\\Innotree\mxt\\function')
