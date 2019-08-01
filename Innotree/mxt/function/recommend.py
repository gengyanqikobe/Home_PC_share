from selenium import webdriver
import time
import sys
import os
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.path_config import mxt_picture_exe_path,mxt_ppt_exe_path,mxt_account_path
from Innotree.mxt.mxt_account_info import get_account_phonenumber,write_account_phonenumber,get_reco_prepare_info
from Innotree.mxt.function.xinyongma import xinyongma
from Innotree.mxt.function.login import Login


class Recommend():
    global bottom
    bottom = "var q=document.documentElement.scrollTop=10000"

    def __init__(self):
        global browser
        get_datas = get_reco_prepare_info()
        self.account = get_datas[0]
        #self.account = 'testaccount10026'
        self.phonenumber = get_datas[1]
        #self.phonenumber = '13062010026'
        self.xinyongma = xinyongma()
        self.corp_name = self.account +'的公司'
        time.sleep(1)



    def in_recommend(self):

        #进入信用认证界面
        self.browser = Login().yonghu(self.account)
        self.browser.implicitly_wait(30)

        self.browser.find_element_by_xpath('/html/body/div/header/div/div[2]/div[2]/a').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/header/div/div[2]/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/a').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[4]/div/div[2]/a').click()
        #向下翻滚
        time.sleep(1)
        self.browser.execute_script(bottom)
        #self.browser.find_element_by_xpath('/html/body/div/div[1]/div/form/div[2]/div/div[2]/div/div[1]/input').send_keys(self.corp_name)
        #self.browser.find_element_by_xpath('/html/body/div/div[1]/div/form/div[2]/div/div[3]/div/div[1]/input').send_keys(self.xinyongma)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/form/div[4]/a').click()
        time.sleep(1)
        return self.browser


    #填写公司基本信息
    def write_com_baseinfo(self,baseinfo):
        self.browser = baseinfo
        #self.browser.get('http://mxt.innotree.cn/auth/recommend/base')
        self.browser.implicitly_wait(30)
        self.browser.execute_script(bottom)
        #-----------------------------------------注册信息
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[1]/div/div/input').send_keys(self.corp_name)
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[2]/div/div/input').send_keys(self.account+'company')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[3]/div/div/input').send_keys(self.xinyongma)
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[4]/div/div[1]/input').send_keys('1000')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[5]/div/div[1]/input').send_keys('1000')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/form/div[1]/div[6]/div/div/input').send_keys('2019-03-03')
        # #输入日期后，点击空白处继续下面的操作
        #self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[6]/label').click()
        time.sleep(1)
        #下拉框，企业类型
        #self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[7]/div/div/div[1]/input').click()
        #self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()

        #下拉框，注册地区
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[8]/div/div/div[1]/div/div/div/input').click()
        # self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[19]/span').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[8]/div/div/div[2]/div/div/div/input').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span').click()
        #
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[9]/div/div/input').send_keys('广东的大事辣子牌坊')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[10]/div/div[1]/input').send_keys('GuangDong')
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[11]/div/div[1]/textarea').send_keys('衣食住行，生活用品')
        # #上传图片。营业执照
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[13]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")#打开autoit生成的程序来上传文件


        #办公环境照
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[14]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[16]/div/div/textarea').send_keys("这是一家公司")
        # #产品介绍，上传ppt
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[17]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
        # #组织架构图
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[18]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[19]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(1)

        #------------------------------------------------------------人员信息

        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/div/input').send_keys(self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[3]/div/div/input').send_keys('110229199656985641')
        # #上传身份证
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[4]/div/div/div[1]/div[2]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[4]/div/div/div[2]/div[2]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[5]/div/div/input').send_keys('100')
        #高管数量
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[6]/div/div/input').send_keys('100')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[7]/div/div/input').send_keys('100')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[8]/div/div/input').send_keys('100')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[9]/div/div/input').send_keys('100')
        #上传花名册
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[10]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)


        #----------------------------------------------------------------核心管理人员信息
        #暂时不填写核心管理人员信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div/div[1]/button').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div/div[3]/div/div[1]/form/div[1]/div/div/input').send_keys('核心人员')
        #

        #------------------------------------------------------------------填报人信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[1]/div/div/input').send_keys(self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[2]/div/div[1]/input').send_keys(self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[3]/div/div/input').send_keys('技术部')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[4]/div/div/input').send_keys('technology')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[5]/div/div/input').send_keys('测试')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[6]/div/div/input').send_keys('QA')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[7]/div/div/input').send_keys(self.phonenumber)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[10]/div/div/input').send_keys('广州市银座大厦')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[11]/div/div/input').send_keys('GuangzhouMall')

        #下一步
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/a[1]').click()
        time.sleep(1)
        return self.browser


    def write_zizhi(self,a):
        self.browser = a

        #----------------------------------专利信息
        self.browser.implicitly_wait(30)

        self.browser.execute_script(bottom)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/button').click()
        # #专利证书名称
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys(self.account+'的专利')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[2]/div/div/input').send_keys('zhuanli'+self.phonenumber)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys(self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[4]/div/div/input').send_keys(self.phonenumber)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[5]/div/div/input').send_keys(self.account)
        # self.browser.execute_script(bottom)
        # #专利申请日，下拉框
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/div/div/input').send_keys('2019-03-26')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/label').click()
        # #授权公告日
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[7]/div/div/input').send_keys('2019-03-26')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/label').click()
        #
        # #专利类型
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[8]/div/div/div/input').click()
        # self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        # #专利状态
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[9]/div/div/label[1]/span[1]/span').click()
        # #上传照片
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[10]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # #保存
        # time.sleep(3)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[2]/button').click()
        # time.sleep(2)
        # #---------------------------------商标信息
        # self.browser.execute_script(bottom)
        #
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/button').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys('商标'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[2]/div/div/input').send_keys(self.account)
        # #下拉框
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys('2018-03-26')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[4]/div/div/input').send_keys('2019-12-12')
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[5]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(3)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/button').click()
        # time.sleep(2)
        #
        # #---------------------------------高新技术企业认定信息
        # #证书编号
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input').send_keys('bianhao'+self.phonenumber)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div/input').send_keys('2019-03-03')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[3]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[4]/div/div/input').send_keys('2020-03-03')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[3]/label').click()
        #
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[5]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # #self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/button').click()
        # time.sleep(1)
        #
        # #self.browser.execute_script(down1200)
        #
        # #----------------------------------质量认证
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[2]/div/div/div/input').click()
        # self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]/span').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[3]/div/div/input').send_keys('高')
        # #证书编号
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[4]/div/div[1]/input').send_keys(self.phonenumber)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[5]/div/div/input').send_keys('2020-03-03')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[2]/div[5]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[6]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        #
        # #------------------------------------外贸产品认证信息
        # #产品认证类型：
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/input').click()
        # self.browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[3]/span').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[3]/div/div/input').send_keys('产品名称'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[4]/div/div/input').send_keys('english'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[5]/div/div/input').send_keys('证书编号'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[6]/div/div/input').send_keys('2020-03-03')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[3]/div[6]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[7]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        #
        # #self.browser.execute_script(down2000)
        #
        # #------------------------------------进出口资质信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[4]/div[2]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(1)
        #
        # #self.browser.execute_script(down3000)
        #
        # #--------------------------------------- 外贸业务相关行政许可信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[2]/div/div/input').send_keys('许可证'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[3]/div/div/input').send_keys('编号'+self.account)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[4]/div/div/input').send_keys('2019-12-12')
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[5]/div[4]/label').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[5]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        # time.sleep(2)

        #下一步
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[6]/a[2]').click()
        time.sleep(1)
        return self.browser


    def write_jingying(self,c):
        #调试时加入
        # self.browser = Login().yonghu(self.account)
        # time.sleep(2)
        # self.browser.get('http://mxt.innotree.cn/auth/recommend/manage')
        # time.sleep(2)

        #调试时注释掉
        self.browser = c
        self.browser.implicitly_wait(30)
        self.browser.execute_script(bottom)
        #--------------------------------------------业务信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div/div/div[1]/input').click()
        # self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        # #近一年出口国家
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/button').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/ul/li[10]/label/span[1]/span').click()
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[2]/button').click()
        # #海外控股子公司
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div/input').send_keys('10')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[4]/div/div/input').send_keys('10')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[5]/div/div/input').send_keys('10')

        #常用价格
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[6]/div/div[1]/div/input').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[6]/div/div[2]/div/input').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
        # #合格率
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[7]/div/div/input').send_keys('1')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[8]/div/div/div[1]/input').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]/span').click()

        #------------------------------------------------产品信息
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[1]/button').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys("产品名称"+self.account)
        #HS编码
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys("HS"+self.account)
        #保存
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/button').click()

        #--------------------------------------------------供应商稳定性
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[1]/div/div/input').send_keys('1')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[2]/div/div/input').send_keys('1')

        #---------------------------------------------------客户稳定性
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/div/input').send_keys('1')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[4]/div[2]/div/div/input').send_keys('1')

        #下一步
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/a[2]').click()
        time.sleep(1)
        return self.browser


    def write_caiwu(self,d):
        self.browser = d
        self.browser.implicitly_wait(30)
        #----------------------------------------------------核心信息
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div[1]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div[1]/div/button').click()
        # os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
        # time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[1]/button').click()
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[1]/div/div/div/input').send_keys('10')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[2]/div/div/div/input').send_keys('20')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[3]/div/div/div/input').send_keys('30')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[3]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[3]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[3]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[4]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[4]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[4]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[5]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[5]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[5]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[6]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[6]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[6]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[7]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[7]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[7]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[8]/div/div[1]/div/div/div/input').send_keys('10')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[8]/div/div[2]/div/div/div/input').send_keys('20')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[8]/div/div[3]/div/div/div/input').send_keys('30')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[9]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[9]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[9]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[10]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[10]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[10]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[11]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[11]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[11]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[12]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[12]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[12]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[13]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[13]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[13]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[14]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[14]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[14]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[15]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[15]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[15]/div/div[3]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[16]/div/div[1]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[16]/div/div[2]/div/div/div/input').send_keys('40')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[16]/div/div[3]/div/div/div/input').send_keys('40')
        #保存
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/button').click()
        time.sleep(1)

        #下一步
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/a[2]').click()
        time.sleep(1)
        return self.browser


    def write_zongheguanli(self,e):
        self.browser = e
        self.browser.implicitly_wait(30)
        self.browser.execute_script(bottom)
        #-------------------------------------档案管理
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div/div/div/label[1]/span[1]/span').click()
        #--------------------------------------信息化管理
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div/div/div/label[1]/span[1]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)
        time.sleep(1)
        #---------------------------------------供应商管理
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div/div/div/label[1]/span[1]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)
        time.sleep(1)
        #-----------------------------------------客户管理
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div/div/div/label[1]/span[1]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)
        time.sleep(1)
        #---------------------------------------研发产品
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/div/div/div/label[1]/span[1]/span').click()
        #-----------------------------------------产品质量控制
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[6]/div/div/div/label[1]/span[1]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[6]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)
        time.sleep(1)
        #---------------------------------------社会责任
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[7]/div[1]/div/div/label[1]/span[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[7]/div[2]/div/div/label[1]/span[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[7]/div[3]/div/div/label[1]/span[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[7]/div[4]/div/div/label[1]/span[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[7]/div[5]/div/div/div[1]/div/button').click()
        time.sleep(1)
        os.system(mxt_ppt_exe_path)
        time.sleep(1)

        #--下一步
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[8]/a[2]').click()
        time.sleep(1)
        return self.browser


    def write_rongyu(self,f):
        self.browser = f
        self.browser.implicitly_wait(30)
        #-----------------------------------------------------------获奖记录
        time.sleep(2)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[1]/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[1]/div/div/input').send_keys('2019-02-02')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[1]/label').click()

        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[2]/div/div/input').send_keys('获奖'+  self.account)
        #获奖等级
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[4]/div/div/div[1]/input').click()
        self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()

        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[5]/div/div[1]/input').send_keys("权威机构颁发")
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[7]/div/div/div[1]/div/button').click()
        os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(2)
        #保存
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        #-------------------------------------------------------海关信用
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div[1]/input').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
        #证书
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div/div[1]/div/button').click()
        os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(1)

        #---------------------------------------------------------守信红名单
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[2]/div/div/div[1]/div/button').click()
        os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(1)

        #下一步
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/a[2]').click()
        time.sleep(1)
        return self.browser

    def write_jiaofei(self,g):

        #调试时加入
        # self.browser = Login().yonghu(self.account)
        # time.sleep(2)
        # self.browser.get('http://mxt.innotree.cn/auth/recommend/pay')
        time.sleep(2)

        #调试时注释掉
        self.browser = g
        self.browser.implicitly_wait(30)
        #缴费状态和私信里面缴费信息
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        self.browser.get('http://mxt.innotree.cn/user/push/info')

        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div/p').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div/div/p/span[5]/span').click()
        #------------------------------------------------上传缴费信息
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[4]/div/ul/li[1]/div[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/div/div/input').send_keys(self.account+'的账户')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[2]/div/div/input').send_keys(self.phonenumber)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[3]/div/div/input').send_keys('2019-03-03')
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/label').click()
        #上传图片
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[5]/div/div/div[1]/div/button').click()
        os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[6]/div/div/textarea').send_keys('上传缴费信息')
        #保存
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/div[2]/button').click()
        #用户完成推荐用户的缴费信息
        return self.browser



    def shenhe_reco(self,h):
        self.browser = h
        self.browser = Login().shenhe()
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        time.sleep(1)

        #进入基础认证审核页面
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[4]/div/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[4]/ul/li[1]/span').click()
        #搜索页查询要进行操作的公司
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(self.corp_name)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        #点击筛选出的公司
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()

        time.sleep(2)

        self.browser.execute_script(bottom)
        #缴费审核
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        #基本信息
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div/div[2]/div[2]/span').click()
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        #资质信息
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        #经营信息
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[4]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[1]').click()
        time.sleep(1)
        self.browser.execute_script(bottom)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(1)

        #   异常信息
        # self.browser.execute_script(bottom)
        # self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/i').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div/div/button').click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        # time.sleep(3)
        # self.browser.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div[3]/button[2]').click()

        time.sleep(2)
        #财务信息
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div/div[2]/div[5]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        #综合管理
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[6]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)

        #合法
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[7]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        #荣誉记录
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[8]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        return self.browser


    def shenpi_to_fangtan(self,i):
        self.browser = i
        self.browser =Login().shenpi()
        self.browser.implicitly_wait(30)
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[3]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(self.account+'的公司')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()
        time.sleep(1)
        self.browser.execute_script(bottom)
        #添加访谈员和时间
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[1]/div/div/div[1]/div/i').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[1]/div/div/div[2]/ul[2]/li[2]').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[2]/div/div/div[1]/div/i').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/span[5]/em').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/span[27]/em').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/form/div[2]/div/div/div[2]/div/div/div/div[4]/button[3]').click()
        #提交
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        return self.browser


    def fangtan_to_shenpi(self,j):
        self.browser = j

        #登录访谈账户
        self.browser = Login().fangtan()
        self.browser.implicitly_wait(30)
        #进入带访谈页面
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(self.account+'的公司')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()
        time.sleep(1)
        self.browser.execute_script(bottom)
        #进入到访谈记录
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div[2]/form/div[1]/div/div/label[2]/span/input').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div[2]/form/div[2]/div/div/textarea').send_keys('tttttttttttt')
       #上传谈判资料
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div[2]/form/div[3]/div/div/div[1]/div/button').click()
        os.system(mxt_picture_exe_path)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        #进入委员会
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[3]/span').click()
        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(self.account+'的公司')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()
        time.sleep(1)
        #填写评审结果
        self.browser.execute_script(bottom)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[1]/div/div/label[2]/span/input').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/div/textarea').send_keys('kkkkkk')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[3]/div/div/div[1]/div/button').click()
        os.system(mxt_picture_exe_path)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[4]/div/div/div/div/button').click()
        os.system(mxt_picture_exe_path)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[5]/div/button').click()
        return self.browser


    def shenpi_fangtan_chenggong(self,k):
        self.browser = k
        self.browser = Login().shenpi()
        self.browser.implicitly_wait(30)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[4]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/div/input').send_keys(self.account+'的公司')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[5]/div/button').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()
        #审批意见，成功
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[7]/div[2]/form/div[2]/div/button').click()

        #切换成用户角色，进行缴费
        time.sleep(1)
        self.browser = Login().yonghu(self.account)
        self.browser.get('http://mxt.innotree.cn/user/auth/info')
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[4]/div/ul/li[8]/div[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/div/div/input').send_keys(self.account+'的账户')
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[2]/div/div/input').send_keys(self.phonenumber)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[3]/div/div/input').send_keys('2019-03-03')
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/label').click()
        time.sleep(1)
        #上传图片
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[5]/div/div/div[1]/div/button').click()
        os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[6]/div/div/textarea').send_keys('上传缴费信息')
        #保存
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[2]/button').click()

        #切换审批员账户，完成最后确认
        time.sleep(2)
        self.browser = Login().shenpi()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[5]/span').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/div/input').send_keys(self.account+'的公司')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[5]/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div').click()
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[9]/span').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(1)
        self.browser.execute_script(bottom)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/div/div/div/button').click()
        os.sys(mxt_picture_exe_path)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[3]/div/button').click()
        print("%s已经成为推荐认证用户"%(self.account))

