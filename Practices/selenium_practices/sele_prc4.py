from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('http://jianshu.com')
time.sleep(3)

#将页面拖到底部
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)


#淘宝就不可以
browser2 = webdriver.Firefox()
browser2.get('http://taobao.com')
time.sleep(3)
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)