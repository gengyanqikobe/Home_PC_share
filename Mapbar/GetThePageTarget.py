import urllib.request,re
def getHtml(url):
    html = urllib.request.urlopen(url)
    sorce = html.read().decode('utf-8')
    return sorce

def getRange(content):
    start0 = content.find(r'<div class="entry">')
    start1 = content.find(r'<ol>',start0)
    end = content.find(r'</ol>',start1)
    content1 = content[start1:end]
    #print(content1)
    return content1

def getLink(content2):
    #print(type(content2))
    res = re.compile(r'a href="(http.*[.html|.pdf]?)" target=')
    result_link = res.findall(content2)
    #print(result_link)
    return result_link

def getName(content2):
    res = re.compile(r'_blank">(.*?)</a>')
    result_name = res.findall(content2)
    #print(result_name)
    return result_name

if __name__ == "__main__":
    content = getHtml('http://blog.jobbole.com/29281/')
    content2 = getRange(content)
    link = getLink(content2)
    name = getName(content2)

    f = open('C:\\Users\gengyq\Desktop\GetThePageTarget.txt', 'w', encoding='utf-8')  # 后面的encoding 解决遇到的编码问题

    i = 1
    for x, y in zip(name, link):
        f.write(str(i) + ' ' + x + ':' + '\n')
        f.write(y + '\n\n')
        i = i + 1
    f.close()
