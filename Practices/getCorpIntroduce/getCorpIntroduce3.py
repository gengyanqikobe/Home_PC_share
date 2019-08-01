#﻿coding=utf-8

#从职友集查询公司企业简介

####注意需要添加Cookie和user-agent 作为Headers

from bs4 import BeautifulSoup
import requests
import sys,os,time,xlwt,xlrd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
from xlutils.copy import copy
from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains

# soup = BeautifulSoup(str(fcont),"html5lib")
#或者

filename = '耿艳奇第二周.xls'
file =xlrd.open_workbook(filename)
table=file.sheets()[0]
#行列表 第一行
rowlt=table.row_values(0)
#列列表 第一列
collt=table.col_values(0)
#行数
ctrow=table.nrows
#列数
ctcol=table.ncols



file2 = copy(file)
# print ctcol,ctrow

sheet = file2.get_sheet(0)

# excel = xlwt.Workbook()  # 创建一个Excel
# sheet = excel.add_sheet('wiki')  # 在其中创建一个名为hello的sheet
# sheet2 = excel.add_sheet('citynull')  # 在其中创建一个名为hello的sheet
# sheet.write(0, 0,'简介')  # 往sheet里第一行第一列写一个数据


driver = webdriver.Firefox()
driver.implicitly_wait(20)

driver.minimize_window()



try:
    for j in range(1,ctrow):
        if table.cell_value(j,2) == "":

            #print(table.cell_value(j,2))


            gsName=table.row_values(j)[1]
            print(gsName)
            driver.get("https://www.jobui.com/cmp?area=全国")
            time.sleep(1)
            def xpah_sendk(xpath,keystring):
                xname=driver.find_element_by_xpath(xpath)
                xname.send_keys(keystring)
            def xpath_click(xpath):
                xname=driver.find_element_by_xpath(xpath)
                xname.click()


            time.sleep(20)      #为了防止被限制


            xpah_sendk('//*[@id="schbar-form-keyword"]',gsName)
            xpath_click('/html/body/div[2]/div/div/div/form/input[3]')
            time.sleep(1)

            try:

                driver.find_element_by_link_text(gsName).click()
            except Exception as e:
                print("未查到该公司")

            else:
                time.sleep(2)

                try:
                    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/p[3]/span').click()
                except Exception as e:
                    pass


                n = driver.window_handles # 获取当前页句柄
                # print (n)
                driver.switch_to.window (driver.window_handles[1])
                url=driver.current_url
                #print(url)
                Cookie = {

                    'Cookie':'jobui_p=1558409029654_4169404; TN_VisitCookie=5; TN_VisitNum=5; PHPSESSID=n7ffitqolcc2p0n9tjrt462e26; Hm_lvt_8b3e2b14eff57d444737b5e71d065e72=1558409030; Hm_lpvt_8b3e2b14eff57d444737b5e71d065e72=1558409087; jobui_area=%25E5%258C%2597%25E4%25BA%25AC',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'

                }
                recontent=requests.get(url,headers= Cookie)
                #print(recontent)
                #print(recontent.text)
                #print(recontent.content)


                soup = BeautifulSoup(str(recontent.text),"lxml")
                try:


                    #找简介
                    lt= soup.find(class_='mb10 cmp-txtshow')
                    #print(type(lt))
                    str_data = str(lt)
                    temp = str_data.split('textShowMore">')[1]
                    temp2 = temp.split('</p>')[0]
                    #print(temp2)
                except Exception as e:
                    print('没有找到简介')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                #print(lt)
                # slt=[]
                # for i in lt:
                #     print(i)
                #     slt.append(str(i['content']))
                # ss=''.join(slt)
                #slt.append(lt)
                else:


                    ss = ''.join(temp2)
                    sheet.write(j,2,str(ss))
                    sheet.write(j,5,"职友集")


                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

        else:
            print('这家公司查过了')


except Exception as e:
    print(e)
finally:
	file2.save(filename)



