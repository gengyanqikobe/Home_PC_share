from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#通过键盘来 控制滚动页面,只针对内嵌滚动条

browser = webdriver.Firefox()
browser.get("http://taobao.com")
time.sleep(1)
browser.maximize_window()
#class只用选择后面的部分就行了如“J_SearchTab tmall-search-tab”中的“tmall-search-tab”全部的反而搜索不到
tianmao = browser.find_element_by_class_name('tmall-search-tab')
#tianmao = browser.find_element_by_class_name('J_SearchTab tmall-search-tab')
tianmao.click()
print(tianmao.text)

'''
#不能往下滑动页面，都定位不到这个元素
xpath_tar = '*//div[@class="sale-hd"]/div[@id="J_SaleP4p"]/a[@title="挂锁"]'
browser.find_element_by_xpath(xpath_tar).click()
browser.find_element_by_xpath(xpath_tar).send_keys(Keys.DOWN)
time.sleep(1)
'''