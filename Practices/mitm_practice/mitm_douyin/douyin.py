__author__ = 'KOBE'




#练习爬虫下载抖音视频

import requests

#文件路径
location = 'F:\douyin\girls3\\'

num = 1
list_url =[]
def response(flow):
    global num,list_url
    path = 'ixigua'

    #判断url是否包含抖音视频
    if path in flow.request.url and flow.request.url not in list_url:
        print("这是请求的url:",flow.request.url)

        filename = location + str(num) + '.mp4'
        res = requests.get(flow.request.url)
        #开始下载视频
        with open(filename,'ab') as f:
            f.write(res.content)
            f.flush()
            print('下载完成:{}'.format(filename))
            num += 1
        list_url.append(num)
        list_url.append(flow.request.url)
        #print(list_url)

        with open('douyin.txt','a') as h:
            h.write(str(num)+'\n')
            h.write(flow.request.url+'\n')


