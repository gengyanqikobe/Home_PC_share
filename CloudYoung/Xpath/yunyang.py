# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Firefox()
time.sleep(2)
# url = "http://mmc.strongdigit.com/"
time.sleep(3)
driver.maximize_window()
driver.get("http://mmc.strongdigit.com/")
# driver.get(url)
driver.find_element_by_id('userName').send_keys('admin')
driver.find_element_by_id('password').send_keys('yy2018')
driver.find_element_by_id('submit_login').click()

handles = driver.current_window_handle
js = "document.getElementById('ulApps').style.display='block'" #编写JS语句
driver.execute_script(js) #执行JS
time.sleep(3)
driver.find_element_by_id('ulApps').text #定位元素

driver.find_element_by_xpath("//ul[@id='ulApps']/li[1]/ul/li[3]").click()
# time.sleep(5)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
print(driver.title)
# time.sleep(20)
ret = driver.find_element_by_xpath("//ul[@class='page-sidebar-menu ']/li[@class='left-menu solid-bottom-border start active']/a/span[@class='title']").text
# print(ret)

# print(all_handles)    # 打印所有的句柄
# driver.switch_to.window(all_handles[-1])
# print(driver.title)
# driver.find_element_by_xpath("//ul[@id='iframe-ul']/li[2]/a").click()
# driver.find_element_by_xpath("//ul[@id='iframe-ul']/li[2]/ul[@class='sub-menu']/li/a[1]").click()