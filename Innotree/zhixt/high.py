


#完成高级信用认证填报
#调用register进行注册

from Innotree.zhixt.register import reg
from Innotree.zhixt.xinyongma import xinyongma
from selenium import webdriver
from Innotree.zhixt.path_config import mxt_picture_exe_path,mxt_ppt_exe_path
import os

import time


def high_credit():
    data = reg()
    browser = data[0]
    account = data[1]
    print(account)
    phonenumber = data[2]
    xym = xinyongma()
    browser.implicitly_wait(20)
    browser.maximize_window()
    time.sleep(1)

    #进入信用认证
    browser.find_element_by_xpath('/html/body/div/header/div/div[1]/div[2]/a').click()
    time.sleep(1)
    bottom = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(bottom)

    browser.find_element_by_xpath('/html/body/div/header/div/div[1]/div[2]/ul/li[2]/a').click()
    browser.execute_script(bottom)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/button').click()
    time.sleep(1)

    #-------------------------填写基础信息

    #browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/input').send_keys(account + '的公司')
    #browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/input').send_keys('营口忠旺铝业有限公司')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/input').send_keys('测试重复公司2')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[2]/div/div/input').send_keys(xym)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[3]/div/div/div[1]/div/div/input').send_keys(200)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[4]/div/div/div[1]/div/div/input').send_keys(200)
    browser.execute_script(bottom)
    #添加时间
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[5]/div/div/input').send_keys('2019-05-05')
    time.sleep(1)
    #手写输入完信息后点击空白位置
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/h2').click()
    #browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]/div/span')
    #注册地区
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[6]/div/div/div[1]/div/div/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[19]').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[6]/div/div/div[2]/div/div/div[1]/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()

    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[7]/div/div/input').send_keys('广东')
    #企业类型
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[8]/div/div/div/div/div/div[1]/input').click()
    browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
    #经营范围
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[9]/div/div/textarea').send_keys('经营范围包括啦啦啦啦啦啦啦')

    #营业执照
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[10]/div/div/div[1]/div/button').click()
    time.sleep(1)
    os.system(mxt_picture_exe_path)
    #办公环境
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[11]/div/div/div[1]/div/button').click()
    time.sleep(1)
    os.system(mxt_picture_exe_path)
    #企业logo
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div/button').click()
    time.sleep(1)
    os.system(mxt_picture_exe_path)
    #公司介绍
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[13]/div/div[1]/textarea').send_keys('这是一家公司的介绍-这是一次高级认证')
    #组织架构
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div[14]/div/div/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(2)
    #下一步
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/button').click()
    time.sleep(2)



    #--------------------------核心成员

    #核心成员信息
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div/div[1]/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[1]/div/div/input').send_keys('李丽丽')
    #核心信息成员-----职位
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[2]/div/div[1]/input').send_keys('老总')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[3]/div/div/textarea').send_keys('多家总经理经验')
    #保存
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[4]/button').click()
    time.sleep(1)


    browser.execute_script(bottom)

    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[1]/div/div/input').send_keys('li法人')
    #身份证
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[3]/div/div[1]/input').send_keys('123456789123456789')
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(1)

    #员工数量
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[5]/div/div/input').send_keys(20)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[6]/div/div/input').send_keys(20)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[7]/div/div/input').send_keys(20)

    #t填报人信息
    #联系人姓名
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[1]/div/div/input').send_keys('联系人姓名')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[2]/div/div/input').send_keys('财务')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[3]/div/div/input').send_keys('会计')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[4]/div/div/input').send_keys(phonenumber)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[5]/div/div/input').send_keys('010686868686')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[6]/div/div/input').send_keys('100010')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[7]/div/div/input').send_keys('广州广州shoho一层啦啦啦')
    #下一步
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()
    time.sleep(2)




    #-------------------------------资质信息

    #专利信息
    for i in range(0,6):

        browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div/div[1]/button').click()
        time.sleep(1)
        #专利申请号
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[1]/div/div/input').send_keys('CN200810134706.1')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[2]/div/div/input').send_keys('123')
        #专利名称
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[3]/div/div/input').send_keys('图像处理装置、图像处理系统及图像处理方法')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[4]/div/div/input').send_keys('松野下纯一')
        #专利类型
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[5]/div/div/div[1]/input').click()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        #专利申请人
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[6]/div/div/input').send_keys('富士施乐株式会社')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[7]/div/div[1]/input').send_keys('富士施乐株式会社')

        browser.execute_script(bottom)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[8]/div/div/input').send_keys('CN101465944B')

        #专利申请日
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[9]/div/div/input').send_keys('2008-07-18')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[1]/span').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[10]/div/div/input').send_keys('2013-04-01')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[1]/span').click()

        #专利状态
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[11]/div/div/div[1]/input').click()
        browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[2]').click()
        #专利证书
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[12]/div/div/div[1]/div/button').click()
        os.system(mxt_picture_exe_path)
        time.sleep(1)

        #保存专利信息
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[13]/button').click()
        time.sleep(1)

    #-----商标信息
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div/div[1]/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[1]/div/div/input').send_keys('098988')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[2]/div/div/input').send_keys('商标的名称')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[3]/div/div/input').send_keys('李嘎嘎')
    #注册有效期
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[4]/div/div/input').send_keys('2020-05-04')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[1]/span').click()
    #商标注册证书
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[5]/div/div/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(2)

    #保存
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/div[3]/div/div/div[2]/form/div[6]/button').click()
    time.sleep(1)


    #----高薪技术认定信息
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[2]/div/div/input').send_keys('92929929')
    #发证时间
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[3]/div/div/input').send_keys('2019-05-05')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/h2').click()
    #有效期
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[4]/div/div/input').send_keys('2020-05-05')
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/h2').click()
    #证书扫描件
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[5]/div/div/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(2)

    #下一步
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button').click()
    time.sleep(2)





    #------------------------------财务信息

    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div/div/div/div[1]/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(1)
    #--资产统计
    #点击编辑
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[1]/div/div/button').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/div/div/div/input').send_keys(100)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[2]/div/div/div/input').send_keys(200)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/input').send_keys(300)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[4]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[4]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[8]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[8]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[8]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[10]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[10]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[10]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[11]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[11]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[11]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[12]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[12]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[12]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[13]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[13]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[13]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[14]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[14]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[14]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[15]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[15]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[15]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[16]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[16]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[16]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[17]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[17]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[17]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[18]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[18]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[18]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[19]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[19]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[19]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[20]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[20]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[20]/div/div[3]/div/div/div/input').send_keys(600)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[21]/div/div[1]/div/div/div/input').send_keys(400)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[21]/div/div[2]/div/div/div/input').send_keys(500)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[21]/div/div[3]/div/div/div/input').send_keys(600)

    #保存
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[23]/button').click()
    time.sleep(2)
    #提交审核
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/button').click()
    time.sleep(1)
    #确认提交
    browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)

    f = open('zhi_high.txt','a',encoding='utf-8')
    f.write(account + '\n')
    f.close()
high_credit()