import os
#用于完成基础信息认证，推荐认证准备状态
import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.function.recommend_prepare import reco
from Innotree.mxt.path_config import used_path

order = "python " + used_path + "\\baseid_part.py"
print(order)
os.system(order)