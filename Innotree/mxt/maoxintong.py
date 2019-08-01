# -*- coding: utf-8 -*- 

import sys,os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.action_chains import ActionChains

# reload(sys)
# sys.setdefaultencoding('utf-8')


from selenium import webdriver 
import random,time
global driver,rint

rint=random.randint(99999,1000000)
name='gyq'+str(rint)
phone="13000"+str(rint)
print('------------------')
print ('username ',name)
print ('phone no ',phone)
pwd="123456"
dxyzm="8756"
picyzm="1234"
driver = webdriver.Firefox()
ff=open('mxtUser.txt','a')
driver.get("http://mxt.innotree.cn/register")
time.sleep(1)
#driver.get("http://www.baidu.com")
def xpah_sendk(xpath,keystring):
	xname=driver.find_element_by_xpath(xpath)
	xname.send_keys(keystring)
def xpath_click(xpath):
	xname=driver.find_element_by_xpath(xpath)
	xname.click()

driver.maximize_window()	
time.sleep(2)
#注册
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[1]/div/div[1]/input',name)
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[2]/div/div[1]/input',phone)
xpath_click('//*[@id="app"]/div/div/div/div/form/div[3]/div/div/button/span')
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[3]/div/div[1]/div/input',dxyzm)
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[4]/div/div[1]/input',pwd)
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[5]/div/div[1]/input',pwd)
xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[6]/div/div[1]/div[1]/input',picyzm)
time.sleep(2)
xpath_click('//*[@id="app"]/div/div/div/div/form/button/span')
time.sleep(6)

#注册完未登陆时用
# xpath_click('//*[@id="app"]/header/div/div[3]/a[1]')
# xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[1]/div/div[1]/input',phone)
# xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[2]/div/div[1]/input',pwd)
# xpah_sendk('//*[@id="app"]/div/div/div/div/form/div[3]/div/div[1]/div[1]/input',picyzm)
# xpath_click('//*[@id="app"]/div/div/div/div/form/button')
# time.sleep(2)


#登录
# xpah_sendk('//*[@id="app"]/div/div/div[2]/form/div[1]/div/div[1]/input',name)
# xpah_sendk('//*[@id="app"]/div/div/div[2]/form/div[2]/div/div[1]/input',pwd)
# xpah_sendk('//*[@id="app"]/div/div/div[2]/form/div[3]/div/div[1]/div[1]/input',picyzm)

# xpath_click('//*[@id="app"]/div/div/div[2]/form/button')
#普通认证
# driver.get("http://172.29.237.244:2502/#/auth/credit/intro")
#-----------------------------
# driver.get("http://172.29.237.244:2502/#/auth/recommend/bind")

xpath_click('//*[@id="app"]/header/div/div[2]/div[2]/a')
# xpath_click('//*[@id="app"]/header/div/div[2]/div[2]/ul/li[1]/a')
action = ActionChains(driver)
action.move_by_offset(50, 100).perform()
time.sleep(4)
#立即认证
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(4)
# xpath_click('//*[@id="app"]/header/div/div[3]/div[2]/ul/li[1]/a')
xpath_click('//*[@id="app"]/div/div/div[4]/div/div[2]/a')
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
corptt=u"因果树"+str(rint)
#企业类型贸易型
xpath_click('//*[@id="app"]/div/div/form/div[2]/div/div[1]/div/div/label[2]/span[1]/span')
xpah_sendk('//*[@id="app"]/div/div/form/div[2]/div/div[2]/div/div[1]/input',corptt)
xydm='012345678901'+str(rint)
xpah_sendk('//*[@id="app"]/div/div/form/div[2]/div/div[3]/div/div[1]/input',xydm)
xpath_click('//*[@id="app"]/div/div/form/div[4]/a')
#基本信息-注册
#企业名称皮换个、、
jsCode = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(jsCode)
time.sleep(2)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[1]/div/div[1]/input',u'中文公司名称')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[2]/div/div[1]/input','Englishname'+str(rint))
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[3]/div/div[1]/input',xydm)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[4]/div/div[1]/input','100')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[5]/div/div[1]/input','80')
time.sleep(2)
#设置时间

#企业类型
# xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[7]/div/div/div/input')
# xpath_click('/html/body/div[2]/div[1]/div[1]/ul/li[5]/span')


# xpah_sendk('/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]/div','2019-1-1')
# # xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[8]/div/div/div[1]/div/div/div/input')
# for i in range(16):
# 	xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[8]/div/div/div[1]/div/div/div/input',Keys.DOWN)
# xpath_click('/html/body/div[3]/div[1]/div[1]/ul/li[16]/span')
# #点击城市
# xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[8]/div/div/div[2]/div/div/div[1]/input')
# xpath_click('/html/body/div[4]/div[1]/div[1]/ul/li[7]/span')





#企业类型
# xpath_click('//*[@id="app"]/div/div[2]/div/form/div[1]/div[6]/div/div/div/input')
# xpath_click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
# #注册地区
# xpath_click('//*[@id="app"]/div/div[2]/div/form/div[1]/div[7]/div/div[1]/div/input')
# xpath_click('/html/body/div[3]/div[1]/div[1]/ul/li[2]')#天津
#注册地址
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[9]/div/div[1]/input',u'中关村')
# xpah_sendk('',u'中关村')
#注册地址(英文)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[10]/div/div[1]/input','abcd')
#主营业务
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[11]/div/div[1]/textarea','abcd')
#主营业务英文
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[12]/div/div/textarea','abcd')
time.sleep(1)

driver.find_element_by_name("file").send_keys("F:\\pictest.jpg")
#办公环境照片
xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[14]/div/div/div[1]/div/button')
os.system("F:\\py\\pysele\\autoJpg.exe")
# xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[17]/div/div/div[1]/div/button/span','F:\\wordtest.docx')
#产品介绍
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[16]/div/div[1]/textarea',u'公司介绍')
time.sleep(1)


xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[17]/div/div/div[1]/div/button/span')
os.system("F:\\py\\pysele\\autoDoc.exe")
#组织架构图
xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div[18]/div/div/div[1]/div/button/span')
os.system("F:\\py\\pysele\\autoJpg.exe")

xpath_click('//*[@id="app"]/div[1]/div/div[2]/div/form/div[1]/div[19]/div/div/div[1]/div/button/span')
os.system("F:\\py\\pysele\\autoJpg.exe")
#公司介绍
#上传两张图
#法人
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[1]/div/div[1]/input',u'法人')
#证件号
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[3]/div/div[1]/input','410702199012142515')
time.sleep(1)
#身份证
xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[4]/div/div/div[1]/div[2]/div/button/span')
os.system("F:\\py\\pysele\\autoJpg.exe")
xpath_click('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[4]/div/div/div[2]/div[2]/div/button/span')
os.system("F:\\py\\pysele\\autoJpg.exe")

xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[5]/div/div[1]/input','15')

xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[1]/div/div[1]/input',u'因果树')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[2]/div/div[1]/input',u'InnoTree')

xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[3]/div/div[1]/input',u'技术部')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[4]/div/div[1]/input',u'dqd')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[5]/div/div[1]/input',u'大前端')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[6]/div/div/input',u'Dq')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[7]/div/div[1]/input',phone)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[8]/div/div[1]/input',phone)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[9]/div/div[1]/input',phone)
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[10]/div/div[1]/input',u'中关村')
xpah_sendk('//*[@id="app"]/div/div/div[2]/div/form/div[3]/div[11]/div/div[1]/input',u'zgc')
ff.write(phone+'\n')
ff.close()


# driver.close()

