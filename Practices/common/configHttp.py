import requests
#from readConfig.py import ReadConfig
import Practices.readConfig as readConfig


localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global timeout,host
        host = localReadConfig.get_url('baseurl')
        timeout =localReadConfig.get_url('timeout')
        self.datas = {}
        self.params = {}
        self.headers = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = host + url

    def set_headers(self,header):
        self.headers = header

    def set_params(self,param):
        self.params = param

    def set_datas(self,data):
        self.datas = data

    def set_files(self,file):
        self.files = file


    #http请求
    def get(self):
        try:
            response = requests.get(self.url,params=self.params,headers = self.headers,timeout = float(timeout))
            return response
        except TimeoutError:
            print('TimeOut Error')
            return None

    def post(self):
        try:
            response = requests.post(self.url,data=self.datas,headers = self.headers,files = self.files,timeout = float(timeout))
            return response
        except TimeoutError:
            print('TimeOut Error')
            return None


