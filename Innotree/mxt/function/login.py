
import time

from selenium import webdriver
class Login(object):
    global browser

    def __init__(self):
        browser = webdriver.Firefox()
        self.browser = browser
    def shenhe(self):
        self.browser.get('http://ams.innotree.cn/login')
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys('shenhe_geng')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('w123456')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/div[1]/div/input').send_keys('1234')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[5]/button').click()
        time.sleep(4)
        return self.browser

    def shenpi(self):
        self.browser.get('http://ams.innotree.cn/login')
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys('shenpi_geng')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('w123456')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/div[1]/div/input').send_keys('1234')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[5]/button').click()
        time.sleep(4)
        return self.browser

    def fangtan(self):
        self.browser.get('http://ams.innotree.cn/login')
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys('fangtan_geng')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('w123456')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/div[1]/div/input').send_keys('1234')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[5]/button').click()
        time.sleep(4)
        return self.browser

    def yonghu(self,account):
        self.browser.get('http://mxt.innotree.cn/user/auth/info')
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[1]/div/div[1]/input').send_keys(account)
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[2]/div/div[1]/input').send_keys('w123456')

        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div[3]/div/div/div[1]/input').send_keys('1234')
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/button').click()
        self.browser.maximize_window()
        time.sleep(4)
        return self.browser
