import urllib.request
import re

def Gethtml(url):#获取整个网页
    res = urllib.request.urlopen(url)
    result = res.read().decode('utf-8')
    #print(result)
    return result


def GetRange(content):#找到想要的区域
    start0 = content.find(r'<h1 class="title-red">')
    end = content.find(r'<div class="nba-hupu-shows">')
    content1 = content[start0:end]
    #print(content1)
    #print(type(content1))
    return content1
def GetLink(content1):#获取目标url
    reg =re.compile(r'href="(http.*?[.htm|.html])">')
    result_link = reg.findall(content1)
    #print(result_link)
    return result_link
def GetName(content1):#获取目标标题
    reg = re.compile(r'[html|htm]">(.*)</a>')
    result_name = reg.findall(content1)
    #print(result_name)
    return result_name


