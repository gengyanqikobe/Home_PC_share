from selenium import webdriver
import time
import sys
from selenium.common.exceptions import NoSuchElementException

import os
sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.path_config import mxt_account_path
from Innotree.mxt.mxt_account_info import get_account_phonenumber,write_account_phonenumber

#用于在贸信通内网注册账户

class Register(object):
    global get_datas,browser
    def __init__(self):
        get_datas = get_account_phonenumber()
        self.account = get_datas[0]
        self.phone_number = get_datas[1]
        self.mark = get_datas[2]
        print(self.account,self.phone_number)

    def web_rj(self):
        browser = webdriver.Firefox()
        browser.implicitly_wait(30)
        browser.get('http://mxt.innotree.cn/register')
        #browser.find_element_by_class_name('account account__register router-link-exact-active router-link-active')
        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "输入要注册的用户名"]').send_keys(self.account)
        #browser.find_element_by_class_name('el-input__inner').send_keys('test1')

        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "输入要注册的手机号码"]').send_keys(self.phone_number)
        browser.find_element_by_class_name('el-button').click()
        time.sleep(1)
        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "请输入短信验证码"]').send_keys("8756")
        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "密码请设置6-20个字符"]').send_keys("w123456")
        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "请再次确认您的密码"]').send_keys("w123456")
        browser.find_element_by_xpath('//div[@class = "el-input"]/input[@placeholder = "请输入验证码"]').send_keys("1234")
        browser.find_element_by_class_name("override-account-button").click()
        #判断是否注册成功,注册成功才写进账号文档里面
        time.sleep(4)

        try:
            element = browser.find_element_by_xpath('/html/body/div/header/div/div[2]/div[1]/a')
        except NoSuchElementException as e:
            print(e)
        else:

            #将注册的用户信息写入到文档中
            write_account_phonenumber(self.account,self.phone_number,self.mark)
        return browser,self.account,self.phone_number
        #browser.quit()



#get_datas = get_account_phonenumber()

