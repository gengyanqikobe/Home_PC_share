import os
import sys
import configparser
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.path_config import mxt_config_path

class Read_config():
    conf = configparser.ConfigParser()
    conf.read(mxt_config_path)

    def get_DB(self,name):
        value = self.conf.get("DB",name)
        return value



#print(Read_config().get_DB('db_password'))