import time
import os
import sys
import random
sys.path.append('C:\\Users\\hasee\\PycharmProjects')
from Innotree.mxt.hesitate import Hesitate
from Innotree.mxt.function.register import Register


global bottom
bottom = "var q=document.documentElement.scrollTop=10000"

#不唯一的信用码
temp = '1'
for i in range(0,17):

    a = random.randint(0,9)
    temp = str(a)+temp
xinyongma = temp

#创建new_account对象，并执行登录操作
new_account = Register()
login_info = new_account.web_rj()
#加入判断，注册完毕后是否需要继续运行
Hesitate()
#----------------------------------------------进入工作台
#从注册处获得浏览器对象，用户名和电话号码
browser = login_info[0]
browser.maximize_window()
account = login_info[1]
phonenumber = login_info[2]
browser.find_element_by_xpath('//div[@class = "el-badge mark"]/span[@class = "icon__login base-icon__user__login"]').click()
time.sleep(1)
browser.find_element_by_xpath('//ul[@class = "base-header-account--list"]/li[@class = "item-link__sub el-row is-justify-center is-align-middle el-row--flex"]/a[@href = "/user"]').click()
time.sleep(1)
browser.find_element_by_xpath('//ul[@class = "menu el-menu"]/li[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//div[@class = "wrapper"]/div[@class = "empty"]/div[@data-v-1d58de46 =""]').click()
time.sleep(1)
browser.find_element_by_xpath('//a[@data-v-299b7d14 = ""]').click()
time.sleep(1)
browser.find_element_by_xpath('//div[@class = "explain--submit explain--submit__credit"]/a[@data-v-e0c43568 = ""]').click()
time.sleep(1)
down = "var q=document.documentElement.scrollTop=1000"
browser.execute_script(down)

#由于第二次注册时候直接跳到基本信息页面，所以调试时候要注释下面几行

time.sleep(2)
#browser.find_element_by_xpath('//form[@class = "el-form auth-bind-form container el-form--label-right"]/div[2]/div[@class = "list-info"/div[@class = "el-form-item is-required"]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]]').send_keys(account+'的公司')
browser.find_element_by_css_selector('div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)').send_keys(account+'的公司')
#browser.find_element_by_xpath('//div[@class = "el-form-item is-required"]/div[#@class = "el-input"]/input[@placeholder = "请输入..."]').send_keys('123456789123456789')
browser.find_element_by_css_selector('div.el-form-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)').send_keys()
browser.find_element_by_xpath('//div[@class = "form--submit el-row is-justify-center is-align-middle el-row--flex"]/a[@class = ""]').click()





#-----------------------------公司基本信息
time.sleep(3)
down600 = "var q=document.documentElement.scrollTop=600"

browser.execute_script(down600)
time.sleep(1)
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[1]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys(account+'的公司')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[2]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys(account+'company')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[3]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys('123456789123456789')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[4]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys('1000')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[5]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys('1000')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[6]/div[@class = "el-form-item__content"]/div[@class = "el-date-editor el-input el-input--prefix el-input--suffix el-date-editor--date"]/input[@class = "el-input__inner"]').send_keys('2019-03-03')
#browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[6]/div/div/input').send_keys('2019-03-03')

#输入日期后，点击空白处继续下面的操作
browser.find_element_by_css_selector('.auth-form-item__first > h3:nth-child(1)').click()
time.sleep(1)
#下拉框，企业类型
#browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[7]/div/div/div/input').send_keys("中外合资")
#browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[7]/div/div/div/input').send_keys("中外合资")
#browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[7]/div[@class = "el-form-item__content"]/div[@class = "el-select"]/div[@class = "el-input el-input--suffix is-focus"]/input[@class = "el-input__inner"]').send_keys('中外合作')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[7]/div/div/div/input').click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()

#下拉框，注册地区
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[8]/div/div/div[1]/div/div/div/input').click()
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[19]').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[8]/div/div/div[2]/div/div/div/span/span/i').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span').click()


browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[9]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys('广东的大事辣子牌坊')
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[10]/div[@class = "el-form-item__content"]/div[@class = "el-input"]/input[@class = "el-input__inner"]').send_keys('GuangDong')
down1200 = "var q=document.documentElement.scrollTop=1200"
browser.execute_script(down1200)
time.sleep(1)
browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[11]/div[@class = "el-form-item__content"]/div/textarea').send_keys('衣食住行，生活用品')
#上传图片。营业执照
#browser.find_element_by_xpath('//div[@class = "auth-form-item__first"]/div[13]/div[@class = "el-form-item__content"]/div[@class = "base-upload"]/button[@class = "el-upload el-upload--picture"]').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[13]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")#打开autoit生成的程序来上传文件

down2000 = "var q=document.documentElement.scrollTop=2000"
browser.execute_script(down2000)
#办公环境照
browser.find_element_by_css_selector('div.el-form-item:nth-child(15) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[16]/div/div/textarea').send_keys("这是一家公司")
#产品介绍，上传ppt
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[17]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
#组织架构图
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[18]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/div[19]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")


#-----------------------人员信息
down3000 = "var q=document.documentElement.scrollTop=3000"
browser.execute_script(down3000)

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/div/input').send_keys(account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[3]/div/div/input').send_keys('110229199656985641')
#上传身份证
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[4]/div/div/div[1]/div[2]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[4]/div/div/div[2]/div[2]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/div[5]/div/div/input').send_keys('100')

#---------------------------------填报人信息

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[1]/div/div/input').send_keys(account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/input').send_keys(account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[3]/div/div/input').send_keys('技术部')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[4]/div/div/input').send_keys('technology')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[5]/div/div/input').send_keys('测试')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[6]/div/div/input').send_keys('QA')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[7]/div/div/input').send_keys(phonenumber)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[10]/div/div/input').send_keys('广州市银座大厦')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[3]/div[11]/div/div/input').send_keys('GuangzhouMall')
Hesitate()
#------------------------------------下一步
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/a[1]').click()
time.sleep(2)



#=================================资质信息==========================
#----------------------------------专利信息

browser.execute_script(down600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/button').click()
#专利证书名称
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys(account+'的专利')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[2]/div/div/input').send_keys('zhuanli'+phonenumber)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys(account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[4]/div/div/input').send_keys(phonenumber)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[5]/div/div/input').send_keys(account)
browser.execute_script(bottom)
#专利申请日，下拉框
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/div/div/input').send_keys('2019-03-26')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/label').click()
#授权公告日
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[7]/div/div/input').send_keys('2019-03-26')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[6]/label').click()

#专利类型
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[8]/div/div/div/input').click()
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
#专利状态
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[9]/div/div/label[1]/span[1]/span').click()
#上传照片
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[1]/form/div[10]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
#保存
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/div[2]/button').click()
time.sleep(2)
#---------------------------------商标信息
browser.execute_script(bottom)

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/button').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys('商标'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[2]/div/div/input').send_keys(account)
#下拉框
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys('2018-03-26')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[4]/div/div/input').send_keys('2019-12-12')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[3]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/form/div[5]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/button').click()
time.sleep(2)

#---------------------------------高新技术企业认定信息
#证书编号
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input').send_keys('bianhao'+phonenumber)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div/input').send_keys('2019-03-03')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[3]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[4]/div/div/input').send_keys('2020-03-03')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[3]/label').click()

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[5]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
#browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/button').click()
time.sleep(1)

#browser.execute_script(down1200)

#----------------------------------质量认证
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[2]/div/div/div/input').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]/span').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[3]/div/div/input').send_keys('高')
#证书编号
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[4]/div/div[1]/input').send_keys(phonenumber)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[5]/div/div/input').send_keys('2020-03-03')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[2]/div[5]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[6]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)

#------------------------------------外贸产品认证信息
#产品认证类型：
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/input').click()
browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[3]/span').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[3]/div/div/input').send_keys('产品名称'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[4]/div/div/input').send_keys('english'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[5]/div/div/input').send_keys('证书编号'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[6]/div/div/input').send_keys('2020-03-03')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[3]/div[6]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/div[7]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)

#browser.execute_script(down2000)

#------------------------------------进出口资质信息
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[4]/div[2]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)

#browser.execute_script(down3000)

#--------------------------------------- 外贸业务相关行政许可信息
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[2]/div/div/input').send_keys('许可证'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[3]/div/div/input').send_keys('编号'+account)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[4]/div/div/input').send_keys('2019-12-12')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[5]/div[4]/label').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[5]/div[5]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(2)
Hesitate()

#-----------------------------------------下一步
#调试的时候由于数据原因标签位置会变，这两个下一步选择一个
#browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[6]/a[2]').click()
browser.execute_script(bottom)

browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[6]/a[2]').click()

time.sleep(2)
browser.execute_script(bottom)

#==============================================经营信息============================================
#---------------------------------------------业务信息
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div/div/div[1]/input').click()
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
#近一年出口国家
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/button').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/ul/li[10]/label/span[1]/span').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[2]/button').click()
#常用价格
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div[1]/div/span/span/i').click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div[2]/div/input').click()
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]/span').click()

#-----------------------------------------------产品信息
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[1]/button').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[1]/form/div[1]/div/div/input').send_keys("产品名称"+account)
#HS编码
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[1]/form/div[3]/div/div/input').send_keys("HS"+account)
#保存
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/button').click()

Hesitate()
#下一步
time.sleep(1)

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/a[2]').click()
time.sleep(2)


#==================================================财务信息===================================================
#--------------------------------------------------核心信息
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div[1]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\mxt_wendang.exe")
time.sleep(1)
#资产统计
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[1]/button').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[1]/div/div/div/input').send_keys('10')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[2]/div/div/div/input').send_keys('20')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[1]/div/div[3]/div/div/div/input').send_keys('30')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[1]/div/div/div/input').send_keys('40')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div/div/div/input').send_keys('40')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/form/div[2]/div/div[3]/div/div/div/input').send_keys('40')
#保存
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/button').click()
Hesitate()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/a[2]').click()

#========================================================荣誉记录========================================================
#-----------------------------------------------------------获奖记录
time.sleep(2)

browser.execute_script(down600)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[1]/button').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[1]/div/div/input').send_keys('2019-02-02')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[1]/label').click()

browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[2]/div/div/input').send_keys('获奖'+account)
#获奖等级
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[4]/div/div/div[1]/input').click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()
browser.execute_script(down600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[5]/div/div[1]/input').send_keys("权威机构颁发")
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/form/div[7]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(2)
#保存
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[2]/button').click()
time.sleep(1)
#-------------------------------------------------------海关信用
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div[1]/input').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
#证书
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[1]/div[3]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)

#---------------------------------------------------------守信红名单
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[2]/div[2]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)
Hesitate()
#下一步1
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/form/div[3]/a[2]').click()

'''
#================================================================缴费状态=====================================
time.sleep(2)
browser.execute_script(down600)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/button').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/button').click()
time.sleep(1)
#=====================================================================完成=====================================
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div[2]/a').click()

#==================================================================消息推送-未处理消息============================
time.sleep(1)
browser.get('http://mxt.innotree.cn/user/push/info')
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div[3]/table/tbody/tr/td[1]/div/div/p').click()
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div/div/p/span[5]/span').click()
#------------------------------------------------上传缴费信息
time.sleep(1)
browser.execute_script(down600)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[4]/div/ul/li[1]/div[2]').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/div/div/input').send_keys(account+'的账户')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[2]/div/div/input').send_keys(phonenumber)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[3]/div/div/input').send_keys('2019-03-03')
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[1]/label').click()
#上传图片
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[5]/div/div/div[1]/div/button').click()
os.system("C:\\Users\\hasee\Documents\\mxt_tp.exe")
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[1]/form/div[6]/div/div/textarea').send_keys('上传缴费信息')
#保存
browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[2]/div[6]/div/div[2]/button').click()
'''
