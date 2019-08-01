from selenium import webdriver
import time

broswer = webdriver.Firefox()

broswer.get("http://baidu.com")
#百度搜索钱包
#broswer.find_element_by_class_name('search-button').click()
broswer.find_element_by_id('kw').send_keys('钱包')
broswer.find_element_by_id('su').click()
