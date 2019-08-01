from selenium import webdriver
import  time
import autoit
import os
name = input('pls input the name:')
driver = webdriver.Firefox()
time.sleep(2)

driver.get("http://dealer.qa.cloud-young.cn")#从浏览器打开指定网址

#找到用户名，密码，输入值，并点击登录#跳转# 到首页
driver.find_element_by_id('userName').send_keys('10001')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('loginBtn').click()

driver.maximize_window()



#点击应用#跳转到经销商员工管理页面
driver.find_element_by_xpath('//div[@class="top-nav"]/ul[@class="top-nav_main"]/li/a[@class="dropdown-toggle"]').click()
driver.find_element_by_xpath('//ul[@id="initApplication"]/li[1]/a[@target="_blank"]').click()
#跳转到最新句柄
time.sleep(3)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
print(driver.title)

time.sleep(5)


#添加员工
driver.find_element_by_id('addBtn').click()
time.sleep(3)
driver.find_element_by_id('accountName').send_keys(name)
driver.find_element_by_id('mobile').send_keys('15866549965')
driver.find_element_by_id('email').send_keys('888@aaa.com')
driver.find_element_by_id('cutImgBtn').click()#直接上传不能调用windows窗口,使用autoit调用windows窗口上传
os.system('C:\\Users\\hasee\Documents\\autoit_test.exe')#打开在autoit中写的程序上传图片
time.sleep(2)
driver.find_element_by_id('saveImage').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/form/div/div[5]/div/label/span').click()
os.system('C:\\Users\\hasee\Documents\\autoit_test.exe')
time.sleep(2)
driver.find_element_by_id('roleId').click()
driver.find_element_by_id('treeDemo_4_span').click()
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div')
time.sleep(2)
driver.find_element_by_id('bcBtn').click()
time.sleep(1)
driver.find_element_by_id('createBtn').click()
time.sleep(2)
#driver.find_element_by_xpath('//button[@class="btn btn btn-primary"]')
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]').click()


time.sleep(5)


#修改第一个员工信息,
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]/a[1]").click()
time.sleep(2)
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys('12345@new.com')
driver.find_element_by_id('bcBtn').click()
time.sleep(3)
driver.find_element_by_id('createBtn').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]').click()

time.sleep(5)

#查询员工,下拉框两次点击
driver.find_element_by_id('select_roleId').click()
driver.find_element_by_id('treeDemo_4_span').click()
#l两种定位方法
driver.find_element_by_id('select_accountName').send_keys(name)
driver.find_element_by_xpath("//button[@id='searchBtn']").click()
driver.find_element_by_id('searchBtn')

time.sleep(5)
#点击禁用按钮,点击否
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]/a[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@class="modal-footer"]/button[@class="btn default"]').click()
time.sleep(2)
#点击引用按钮，点确认
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]/a[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="modal-footer"]/button[@id="disableBtn"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@class="modal-footer"]/button[@class="btn btn btn-primary"]').click()

time.sleep(3)
#切换到禁用选项卡
driver.find_element_by_id('disableNav').click()

time.sleep(5)
#删除员工
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]/a[3]').click()
driver.find_element_by_id('deleteBtn').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]').click()







