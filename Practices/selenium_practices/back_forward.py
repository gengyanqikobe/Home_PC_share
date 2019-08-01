from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('http://baidu.com')
time.sleep(1)
browser.get('http://taobao.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()