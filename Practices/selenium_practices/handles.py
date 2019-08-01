from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://www.taobao.com')
time.sleep(1)
#新建一个选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
time.sleep(1)

#选择句柄
browser.switch_to.window(browser.window_handles[1])
browser.get('http://baidu.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
time.sleep(1)

#关闭选项卡
browser.close()
browser.window_handles[0]
