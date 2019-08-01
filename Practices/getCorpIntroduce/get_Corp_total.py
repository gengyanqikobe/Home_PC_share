#﻿coding=utf-8

#这是三个源的合集，目的是为了一次性执行，尽可能减少手动时间，减少复制粘贴的整理工作
#只需要将符合格式的文档放进同目录即可，手动修改filename_list中的名称
#由于数据原因，企顺网暂时block掉，

#按照

from bs4 import BeautifulSoup
import requests
import sys,os,time,xlwt,xlrd

import random
from xlutils.copy import copy
from selenium import webdriver



#文件名

#多个人的xls集合，
filename_list = ['wangxinjie.xls','gengyanqi.xls','zhoushuo.xls','gongliangwen.xls','maruiqiang.xls','tangmengping.xls','duyaping.xls']

#通过for循环遍历
for filename in filename_list:

    try:

        file =xlrd.open_workbook(filename)
    except Exception as e:
        print(filename+'不存在')
        #不存在的xls文件直接跳过
        continue
    else:

        table=file.sheets()[0]
        #行列表 第一行
        rowlt=table.row_values(0)
        #列列表 第一列
        collt=table.col_values(0)
        #行数
        ctrow=table.nrows
        #列数
        ctcol=table.ncols

        #print(ctcol,ctrow)


        file2 = copy(file)
        # print ctcol,ctrow

        sheet = file2.get_sheet(0)



        driver = webdriver.Firefox()


        driver.implicitly_wait(3)

        driver.minimize_window()


        #从职友集查询公司企业简介

        try:
            for j in range(1,ctrow):
                #print(j)
                if table.cell_value(j,2) == "":

                    #print(table.cell_value(j,2))


                    #gsName=table.row_values(j)[1]
                    gsName = table.cell_value(j,1)
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
                    xpath_click('/html/body/div[2]/div/div[1]/div/div/form/button')
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

                        else:


                            ss = ''.join(temp2)
                            sheet.write(j,2,str(ss))
                            #sheet.write(j,5,"职友集")

                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                            #每次执行都保存一遍
                            file2.save(filename)

                else:
                    print('这家公司查过了')


        except Exception as e:
            print(e)
        finally:
            file2.save(filename)


    #==========================================================================
    print('搜好货============================================================================================')

    #从搜好货查询公司企业简介
    try:

        file =xlrd.open_workbook(filename)
    except Exception as e:
        print(filename+'不存在')
        continue
    else:
        table=file.sheets()[0]
        #行列表 第一行
        rowlt=table.row_values(0)
        #列列表 第一列
        collt=table.col_values(0)
        #行数
        ctrow=table.nrows
        #列数
        ctcol=table.ncols

        #print(ctcol,ctrow)


        file2 = copy(file)
        # print ctcol,ctrow

        sheet = file2.get_sheet(0)


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
                    time.sleep(1)
                    try:
                        #搜好货格式与其他两家不一样，所以不能用link_text来判断

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
                                #sheet.write(j,5,"搜好货")
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                                #每次执行都保存一遍结果

                                file2.save(filename)
                            else:
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])

                else:
                    print('这家公司已经查过了')

        except Exception as e:
            print(e)
        finally:
            file2.save(filename)
        driver.close()
        print('\n\n'+filename +'\n\n')



    #-----------------------------------------------------------------------------------------------------
    # #从顺企网查询公司企业简介
    # print('顺企网====================================================================================')
    #
    # file =xlrd.open_workbook(filename)
    # table=file.sheets()[0]
    # #行列表 第一行
    # rowlt=table.row_values(0)
    # #列列表 第一列
    # collt=table.col_values(0)
    # #行数
    # ctrow=table.nrows
    # #列数
    # ctcol=table.ncols
    #
    # #print(ctcol,ctrow)
    #
    #
    # file2 = copy(file)
    # # print ctcol,ctrow
    #
    # sheet = file2.get_sheet(0)
    #
    # try:
    #     for j in range(1,ctrow):
    #         if table.cell_value(j,2) == "":
    #             gsName=table.row_values(j)[1]
    #             print(gsName)
    #             driver.get("http://so.11467.com/cse/search?q=&click=1&s=662286683871513660&nsid=1")
    #             time.sleep(1)
    #             def xpah_sendk(xpath,keystring):
    #                 xname=driver.find_element_by_xpath(xpath)
    #                 xname.send_keys(keystring)
    #             def xpath_click(xpath):
    #                 xname=driver.find_element_by_xpath(xpath)
    #                 xname.click()
    #
    #
    #             time.sleep(90)
    #
    #             xpah_sendk('//*[@id="kw"]',gsName)
    #             xpath_click('//*[@id="su"]')
    #
    #             time.sleep(1)
    #             try:
    #
    #                 driver.find_element_by_link_text(gsName).click()    #用这个方法可以成功找到想要的链接
    #
    #             except Exception as e:
    #                 print("未查到该公司")
    #
    #
    #             else:
    #                 time.sleep(2)
    #                 n = driver.window_handles # 获取当前页句柄
    #                 # print (n)
    #                 driver.switch_to.window (driver.window_handles[1])
    #                 url=driver.current_url
    #                 #print(url)
    #                 recontent=requests.get(url)
    #                 #print(recontent)
    #                 #print(recontent.text)
    #                 #print(recontent.content)
    #                 time.sleep(1)
    #                 try:
    #                     xpath_click('/html/body/div[4]/div[1]/div[2]/div/div[1]/a')
    #                 except Exception as e:
    #                     pass
    #                 time.sleep(10)
    #
    #                 soup = BeautifulSoup(str(recontent.text),"lxml")
    #
    #                 try:
    #                     lt= soup.find('div',attrs={'id':"aboutuscontent"})
    #                     #print(lt)
    #                     str_data = str(lt)
    #                     temp = str_data.split('"aboutuscontent">')[1]
    #                     temp2 = temp.split('</div>')[0]
    #                     print(temp2)
    #                 except Exception as e:
    #                     print('没有找到简介')
    #                     driver.close()
    #                     driver.switch_to.window(driver.window_handles[0])
    #                 #print(lt)
    #                 # slt=[]
    #                 # for i in lt:
    #                 #     print(i)
    #                 #     slt.append(str(i['content']))
    #                 # ss=''.join(slt)
    #                 #slt.append(lt)
    #                 else:
    #
    #
    #                     ss = ''.join(temp2)
    #                     sheet.write(j,2,str(ss))
    #                     sheet.write(j,5,"顺企网")
    #                     driver.close()
    #                     driver.switch_to.window(driver.window_handles[0])
    #
    #         else:
    #             print('这家公司已经查过了')
    #
    #
    # except Exception as e:
    #     print(e)
    # finally:
    # 	file2.save(filename)


    #


