

#-----------数字园区注册


import time
from selenium import webdriver
import random
def register():

    browser = webdriver.Firefox()
    url = 'http://park.innotree.com/register'
    browser.get(url)



    browser.implicitly_wait(20)
    browser.maximize_window()


    acc_num = random.randint(1000000,9999999)
    str_acc_num = str(acc_num)
    account = 'shu_test' + str_acc_num

    phonenumber = '1444' + str_acc_num
    print(phonenumber)

    #zhanghu
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[1]/div/div/input').send_keys(account)
    #用户类型，园区先不填写

    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[4]/div/div[1]/input').send_keys(phonenumber)
    #点击发送短信
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[5]/div/div/button').click()

    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[5]/div/div/div/input').send_keys('8756')
    #Mima
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[6]/div/div/input').send_keys('w123456')
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[7]/div/div/input').send_keys('w123456')

    #点击注册
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/button').click()
    time.sleep(3)
    browser.close()

    return account,phonenumber

#register()