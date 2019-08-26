__author__ = 'KOBE'



from appium import webdriver
from time import sleep


class Action():
    def __init__(self):
        self.devices_caps = {
            "platformName": "Android",
            "deviceName": "Redmi 4X",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
            "platformVersion": "6.0.1",
            "unicodeKeyboard":True,
            "resetKeyboard":True
        }
        self.server = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(self.server,self.devices_caps)
        self.driver.implicitly_wait(5)

    def massage(self):
        #清楚“我知道了”以及点按操作
        # 设置滑动初始坐标和滑动距离
        self.start_x = 355
        self.start_y = 900
        self.distance = 700

        self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)
        sleep(6)
        try:
            self.driver.find_element_by_id('y7').click()
        except Exception as e:
            print('没有定位到,我知道了')
        sleep(1)
        self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)

    def search(self):
        #搜索要找到视频种类
        sleep(2)
        #进入搜索页面
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/azj').click()
        sleep(10)
        #搜索美女
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/aar').click()
        sleep(2)
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/aar').send_keys('外国美女')
        sleep(2)
        #点击搜索
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/dis').click()
        sleep(5)
        #切换到视频页
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]').click()
        sleep(3)
        #选择一个视频
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]').click()



    def login(self):
        #app登录
        sleep(2)
        #进入到模块“我”
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.DmtViewPager.MyAccessibilityDelegate/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView').click()
        sleep(1)
        #选择账号密码登录
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').click()
        sleep(1)
        #输入用户名密码
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8y').send_keys(15811060061)
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8x').send_keys('douyin123')
        sleep(1)
        #同意条款
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/c6_').click()
        sleep(1)
        #登录
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/od').click()


    def scroll(self):
        #无限滑动
        sleep(1)
        while True:
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)
            sleep(8)
    def main(self):
        #self.comments()
        self.massage()
        self.login()
        self.search()
        self.scroll()

if __name__ == '__main__':
    action = Action()
    action.main()