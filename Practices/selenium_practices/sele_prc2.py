from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('http://www.taobao.com')
time.sleep(1)
#browser.find_element_by_class_name('search-button').click()

#css这个.代表class,[]代表你输入任意的，#代表id
#browser.find_element_by_css_selector(".btn-login ml1 tb-bg weight").click()

#browser.find_element_by_css_selector("[name=登录]").click()

#还是xpath直接用比较好使
print(browser.find_element_by_xpath('*//div[@class="member-logout J_MemberLogout"]/a[@class="btn-login ml1 tb-bg weight"]').text)
browser.find_element_by_xpath('*//div[@class="member-logout J_MemberLogout"]/a[@class="btn-login ml1 tb-bg weight"]').click()

