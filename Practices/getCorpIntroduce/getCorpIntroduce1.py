#﻿coding=utf-8

#从搜好货查询公司企业简介

from bs4 import BeautifulSoup
import requests
import sys,os,time,xlwt,xlrd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from xlutils.copy import copy


from selenium.webdriver.common.action_chains import ActionChains

# soup = BeautifulSoup(str(fcont),"html5lib")
#或者


filename = '耿艳奇第二周.xls'

file=xlrd.open_workbook(filename)
table=file.sheets()[0]
#行列表 第一行
rowlt=table.row_values(0)
#列列表 第一列
collt=table.col_values(0)
#行数
ctrow=table.nrows
#列数
ctcol=table.ncols

# print ctcol,ctrow

file2 = copy(file)

sheet = file2.get_sheet(0)

driver = webdriver.Firefox()

driver.minimize_window()


try:
    for j in range(1,ctrow):
        if table.cell_value(j,2) == "":

            gsName=table.row_values(j)[1]
            print(gsName)
            driver.get("http://www.912688.com/gongshang")
            time.sleep(1)
            def xpah_sendk(xpath,keystring):
                xname=driver.find_element_by_xpath(xpath)
                xname.send_keys(keystring)
            def xpath_click(xpath):
                xname=driver.find_element_by_xpath(xpath)
                xname.click()




            xpah_sendk('/html/body/div[4]/div/div/input',gsName)
            xpath_click('/html/body/div[4]/div/div/button')
            time.sleep(2)
            try:

                xpath_click('/html/body/div[6]/div[1]/div[1]/h3/a')
            except Exception as e:
                print("未查到该公司")

            else:
                time.sleep(2)
                n = driver.window_handles # 获取当前页句柄
                # print (n)
                driver.switch_to.window (driver.window_handles[1])
                url=driver.current_url
                # print url
                recontent=requests.get(url)
                # print type(recontent)
                #print(recontent.text)
                #print(recontent.content)


                soup = BeautifulSoup(str(recontent.text),"lxml")
                try:
                    #获取公司名称
                    corp_name = soup.find(class_ = 'com-name-box')
                    str_corp_name = str(corp_name)
                    temp_name = str_corp_name.split('<h1>')[1]
                    temp_name2 = temp_name.split('</h1')[0]


                    #获取介绍
                    lt= soup.find(class_= 'detail-info')
                    #print(type(lt))
                    str_data = str(lt)
                    temp = str_data.split('<p>')[1]
                    temp2 = temp.split('</p>')[0]
                    #print(temp2)
                except Exception as e:
                    print('没有找到简介')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                else:
                    if temp_name2 == gsName:

                        ss = ''.join(temp2)
                        sheet.write(j,2,str(ss))
                        sheet.write(j,5,"搜好货")

                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    else:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

        else:
            print('这家公司已经查过了')

except Exception as e:
    print(e)
finally:
	file2.save(filename)



