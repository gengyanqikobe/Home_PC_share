



#控制浏览器的时候使用下面的语句
#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  --proxy-server=127.0.0.1:8080 --ignore-certificate-errors

from mitmproxy import ctx
import mitmproxy

class Cute:
    def request(self,flow: mitmproxy.http.HTTPFlow):

        if flow.request.host != 'www.baidu.com':
            return
        ctx.log.info("发现有人搜索：%s" % flow.request.query.get('wd'))
        flow.request.query.set_all('wd',['最可爱的人'])


    def response(self,flow : mitmproxy.http.HTTPFlow):
        text = flow.response.get_text()
        text = text.replace("最可爱的人","最可爱的人是巨魔")
        flow.response.set_text(text)

addons = [
    Cute()
]