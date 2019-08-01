#coding=utf-8
from selenium import webdriver
import time
import os
import requests
import subprocess
from urllib.request import urlretrieve
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#本py，第一是用来识别贸信通登录中验证码
#第二是用来取得token来给新杰的接口调用
#注意self中初始化browser会打开多个浏览器
#当browser.clear()不起作用，可以选择keys来完成删除操作

class Picture():

    def __init__(self):
        self.Status = False#判断程序是否结束



    def open_web(self):#打开贸信通线上地址，输入用户名密码
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

        self.browser.get('http://www.trustrader.cn/login')
        self.browser.implicitly_wait(20)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[4]/div/label/span[1]/span').click()
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').send_keys('13520874283')
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').send_keys('123456')


        return self.browser

    def get_img_url(self,browser):#跟进xpath和attribute找到验证码的地址
        self.browser = browser

        img = self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[2]/img')

        target_url = img.get_attribute("src")
        #print(target_url)
        return  target_url,self.browser

    def get_text(self,target_url):#通过urlretrieve下载验证码，由于requests.get必须是http开头标准的
            #通过os。system调用tesseract识别图片，写入文本并return


        urlretrieve(target_url,'123.jpg')

        os.system('tesseract 123.jpg test digits')#加上digits只识别英文和数字

        f = open('test.txt','r',encoding='utf-8')
        data = f.readlines()
        try:
            text = data[0]
        except Exception as e:
            print(e)
        else:

            print(text)
            return text

    def login(self,text,browser):#登录，传入验证码text，登录成功后寻找token，访问新杰的连接，不成功刷新验证码，再次识别
        self.browser = browser

        if text !=None:
            time.sleep(2)
            # #self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').clear()
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').send_keys(Keys.CONTROL+'a')
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').send_keys(Keys.BACKSPACE)
            # time.sleep(2)
            #
            # time.sleep(2)
            # #self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').clear()
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').send_keys(Keys.CONTROL+'a')
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').send_keys(Keys.BACKSPACE)
            # time.sleep(2)

            time.sleep(2)
            #self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').clear()
            self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').send_keys(Keys.CONTROL+'a')
            self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').send_keys(Keys.BACKSPACE)

            time.sleep(1)
            self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').send_keys(text)


            time.sleep(1)
            self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/button').click()



            time.sleep(5)
            try:

                temp_data = self.browser.current_url
                #print(temp_data)
            except Exception as e:
                print("login failed,try once again")
            else:
                if temp_data == u"http://www.trustrader.cn/":
                    self.Status ==True
                    cookie_list = self.browser.get_cookies()
                    print("this is cookie list",cookie_list)
                    for cookie in cookie_list:
                        if cookie['name'] == 'token':
                            print("this is cookie:",cookie['value'])
                            forXinJie = webdriver.Firefox()
                            xinjie_url = 'http://172.28.102.148:2500/innotreetest/token?token='+cookie['value']
                            js = "window.open('+xinjie_url+')"
                            forXinJie.get(xinjie_url)
                            return cookie['value']

                else:
                    self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[2]/img').click()
                    # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').clear()
                    # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').clear()
                    # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').clear()
                    Picture().run_above(self.browser)
                    time.sleep(1)

            time.sleep(3)
        else:

            self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[2]/img').click()
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').clear()
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').clear()
            # self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').clear()

            Picture().run_above(self.browser)
            time.sleep(1)


    def run_above(self,browser):

        if self.Status == False:

            temp_data = Picture().get_img_url(browser)
            url = temp_data[0]
            browser = temp_data[1]

            text = Picture().get_text(url)

            cookie = Picture().login(text,browser)
            print('run_cookie:',cookie)
            return cookie


browser = Picture().open_web()

cookie_result = Picture().run_above(browser)
print('true-cookie',cookie_result)



