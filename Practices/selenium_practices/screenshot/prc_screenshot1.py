


from selenium import webdriver
import time


url = "https://bbs.hupu.com/28040620.html"
'''
browser = webdriver.Firefox()
#-------------------------------普通版本，不能截取长图
browser.get(url)
browser.maximize_window()
browser.implicitly_wait(50)

browser.get_screenshot_as_file('1.png')
'''

#----------------------使用phantomjs能够截取长图
browser2 = webdriver.PhantomJS()

browser2.get(url)
browser2.implicitly_wait(50)
browser2.maximize_window()
browser2.get_screenshot_as_file('22.png')
