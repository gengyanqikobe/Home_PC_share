__author__ = 'KOBE'




#练习爬虫下载抖音视频

import requests

#文件路径
location = 'E:\douyin\girls\\'

num = 1
def response(flow):
    global num
    path = 'ixigua'
    #判断url是否包含抖音视频
    if path in flow.request.url:
        filename = location + str(num) + '.mp4'
        res = requests.get(flow.request.url)
        #开始下载视频
        with open(filename,'ab') as f:
            f.write(res.content)
            f.flush()
            print('下载完成:{}'.format(filename))
            num += 1

