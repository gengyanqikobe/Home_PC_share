import re
import webbrowser

import GetKobeFromHupu


con = GetKobeFromHupu.Gethtml('https://nba.hupu.com/')
str_a = GetKobeFromHupu.GetRange(con)
reg = re.compile(r'href="(http.*?[.html|.htm]">.*?)/a>')#把url和标题都取出来
res = reg.findall(str_a)
#for item in res:
    #print(item)
#print(len(res))

reg1 = re.compile(r'(http.*?[.html|.htm])">')#再从取出来的整体里面取出url
res1 = reg1.findall(str(res))
#for item in res1:
    #print(item)
#print(len(res1))

reg2 = re.compile(r'">(.*?)<')
res2 = reg2.findall(str(res))
#for item in res2:
    #print(item)
#print(len(res2))

dict_res = dict(zip(res2,res1))
#print(dict_res)
f = open('C:\\Users\hasee\Desktop\kobefromhupu.txt','r',encoding='utf-8')

#创建一个list表来存储要查询的关键字
list_keyword = []
n = 0
m = int(input('请输入搜索的关键字的个数：'))
while n < m :
    keyword = input('请输入关键字：')
    list_keyword.append(keyword)
    n= n + 1
list_url = []#用来存放将要在浏览器中打开的url
lines = f.readlines()
f.close()

i = 0#url的数量
f = open('C:\\Users\hasee\Desktop\kobefromhupu.txt','a',encoding='utf-8')
for item in dict_res.keys():
    for keyw in list_keyword:#取关键字在name中遍历
        if keyw in item:
            f.write('\n'  + ' ' + item + '\n' + dict_res[item] + '\n\n')
            list_url.append(dict_res[item])
            #print(item)
            i = i + 1

#f.write(str(i) )
f.close()
#print(list_url)
status = True
for url in list_url:
    while status ==True:
        a = input("you have "+str(i)+" web have to see,type  'y' to continue,type 'n' to leave it away \n ")
        if a == 'y':
            webbrowser.open(url)  #通过浏览器打开得到的url
            i = i-1
            status = True
            break
        elif a =='n' or i == 0:
            status = False
            break

        else:
            print("pls type the correct litter ")
            status =True
    if status ==False:
        print('over')
        break









