from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.get('http://taobao.com')

print(browser.title)
#先调用EC赋值给title
title = EC.title_is(u'淘宝网 - 淘！我喜欢')
#title和browser的title进行对比
print('EC.title_is:',title(browser))


title_cantains = EC.title_contains(u'淘宝网')
print('EC.title_contains:',title_cantains(browser))


duihuakuang = EC.presence_of_element_located((By.ID,'q'))
print('EC.presence_of_element_located',duihuakuang)


