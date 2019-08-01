from selenium import webdriver
import time
#打开一个网页
browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
time.sleep(2)

print(browser.page_source)

browser.close()