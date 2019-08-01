import os
import Practices.readConfig as readConfig
import pymysql

localReadConfig = readConfig.ReadConfig()

class MyDB:
    global host,username,password,port,config
    host = localReadConfig.get_database('db_host')
    username = localReadConfig.get_database('db_username')
    password = localReadConfig.get_database('db_password')
    port = localReadConfig.get_database('db_port')
    config = {
        'host' : str(host),
        'user' : str(username),
        'passwd': str(password),
        'port' : int(port)
    }

    def connectDB(self):
        try:
            #建立数据库连接
            self.db = pymysql.connect(**config)
            cursor = self.db.cursor()

        except ConnectionError :
            print(ConnectionError)