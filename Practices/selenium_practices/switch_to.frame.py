from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

#从一个框架跳到另一个框架
browser = webdriver.Firefox()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

browser.switch_to.frame('iframeResult')
#source = browser.find_element_by_css_selector('#draggable')
source = browser.find_element_by_id('draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print("This Frame No Logo")

browser.switch_to.parent_frame()
try:
    #logo = browser.find_element_by_class_name('navbar-header logo')
    logo = browser.find_element_by_xpath('*//div[@class="container"]/div[@class="navbar-header logo" ]')
    #browser.find_element_by_xpath('*//div[@class="member-logout J_MemberLogout"]/a[@class="btn-login ml1 tb-bg weight"]').click()

    print(logo)
    print(logo.text)
    logo.click()
except NoSuchElementException:
    print("This Frame No Logo Too")

