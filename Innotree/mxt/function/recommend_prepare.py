from selenium import webdriver
import time
import sys
import os

sys.path.append("C:\\Users\\hasee\\PycharmProjects")
from Innotree.mxt.db_sql.update_grade import update_grade
from Innotree.mxt.path_config import mxt_picture_exe_path
from Innotree.mxt.function.login import Login

def reco(account,phonenumber):
    #corp_name = input("请输入企业名称：")
    corp_name = account +'的公司'
    #corp_name = '北京颖泰嘉和生物科技股份有限公司'
    bottom = "var q=document.documentElement.scrollTop=10000"
    browser = webdriver.Firefox()
    browser.get("http://ams.innotree.cn/login")
    browser.implicitly_wait(30)
    browser.maximize_window()
    #登录审核员账户
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys('shenhe_geng')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('w123456')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/div[1]/div/input').send_keys('1234')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[5]/button').click()
    time.sleep(2)

    #进入基础认证审核页面
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[3]/div').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[3]/ul/li[1]/span').click()
    #搜索页查询要进行操作的公司
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(corp_name)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()


    time.sleep(2)

    browser.execute_script(bottom)
    #缴费审核
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/span').click()
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(1)
    #基本信息
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div/div[2]/div[2]/span').click()
    browser.execute_script(bottom)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    #资质信息
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/span').click()
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(1)
    #经营信息
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[4]/span').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[1]').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div/button').click()
    time.sleep(2)

    #   异常信息
    browser.execute_script(bottom)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/i').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div/div/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div[3]/button[2]').click()

    time.sleep(2)
    #财务信息
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div/div[2]/div[5]/span').click()
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[6]/span').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[1]/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div/div/div[3]/button[2]').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()


    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div[7]/span').click()
    browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(1)
    #切换到审批员账号
    browser.quit()
    browser = webdriver.Firefox()
    browser.get('http://ams.innotree.com/login')
    time.sleep(1)
    #登录审批员账号
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys('shenpi_geng')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('w123456')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/div[1]/div/input').send_keys('1234')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/form/div[5]/button').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/span').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys(corp_name)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/div/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span').click()
    browser.execute_script(bottom)
    #修改企业评分
    update_grade(corp_name)
    time.sleep(1)
    #上传证书
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[2]/div/div/div/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[3]/div/div/div/div/button').click()
    os.system(mxt_picture_exe_path)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[6]/div[2]/form/div[5]/div/button').click()
    print('基础认证完成，可以进行推荐认证')


#reco('testaccount10049','13062010049')