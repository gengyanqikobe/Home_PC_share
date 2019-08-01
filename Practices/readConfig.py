
import os
import configparser
#获得当前文件目录的父级
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,'config.ini')


class ReadConfig:

    #def __init__(self):

        #self.cf = configparser.ConfigParser()
#读取config
        #self.cf.read('config.ini')

#查看config里面所有的元素
       # for sec in self.cf.sections():
       #     print(self.cf.items(sec),sec)
    cf = configparser.ConfigParser()
    cf.read(configPath)


    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value

    def get_database(self,name):
        value = self.cf.get("DATABASE",name)
        return value

    def get_url(self,name):
        value = self.cf.get("HTTP",name)
        return value


#print(ReadConfig().get_url('timeout'))
