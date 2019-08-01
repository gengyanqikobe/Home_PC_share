

from selenium import webdriver
import time
import random




def reg():
    browser = webdriver.Firefox()
    browser.implicitly_wait(20)
    browser.get('http://xin.innotree.com/register')

    acc_num = random.randint(1000000,9999999)
    str_acc_num = str(acc_num)
    account = 'zhi_test' + str_acc_num

    phonenumber = '1484' + str_acc_num
    print(phonenumber)

    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[1]/div/div/input').send_keys(account)
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[2]/div/div/input').send_keys(phonenumber)

    #输入验证码
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[3]/div/div/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[3]/div/div/div/input').send_keys('8756')
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[4]/div/div/input').send_keys('w123456')
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[5]/div/div/input').send_keys('w123456')
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[6]/div/div/div/input').send_keys('1234')
    time.sleep(1)
    #点击登录
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/button').click()
    time.sleep(4)
    #print(browser.current_url)

    if browser.current_url == 'http://xin.innotree.com/':


        f = open('zhixt_account.txt','a',encoding='utf-8')
        f.write(account +'\n')
        f.write(phonenumber + '\n\n')
        f.close()
    else:
        print("注册失败")

    return browser,account,phonenumber
#如果只需要注册的话，恢复下面的注释，使用完毕后注释上即可
    #browser.close()

# for i in range(0,20):
#     reg()