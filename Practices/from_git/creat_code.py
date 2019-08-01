import os
import time
import random

#本文件可以生成一个12位包含字母和大小写的密码

def creat_code():


    str1 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
    status = False
    len_str1 = len(str1)
    #print(len_str1)http://xin.innotree.com/search/detail/tag/relation/corp/list?tagName=%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%BA%A7%E4%B8%9A

    while status == False:
        code = ''           #每次要给code清空
        for i in  range(0,10):
            j = random.randint(0,len_str1-1)
            #print("j",j)
            a = str1[j]
            code += a
            #print(a)
        #print(code)
        #判断是否包含三中元素
        for i in '1234567890':

            if i in code:
                #print('有数字')
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j in code:
                        #print('有小写字母')
                        for k in 'ABCDEFGHIGKLMNOPQRSTUVWXYZ':
                            if k in code:
                                #print('有大写字母')
                                status = True
        #time.sleep(1)

    return code


code = creat_code()
print(code)
