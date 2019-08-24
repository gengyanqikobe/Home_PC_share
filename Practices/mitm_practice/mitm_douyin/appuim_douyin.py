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
            "platformVersion": "6.0.1"
        }
        self.server = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(self.server,self.devices_caps)

        # 设置滑动初始坐标和滑动距离
        self.start_x = 355
        self.start_y = 900
        self.distance = 700

        sleep(10)
        try:
            self.driver.find_element_by_id('y7').click()
        except Exception as e:
            print('没有定位到,我知道了')
    """
    def comments(self):
        sleep(3)
        #点击一次屏幕
        self.driver.tap([(500, 1200)], 500)
    """


    def scroll(self):
        #无限滑动
        while True:
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)
            sleep(10)
    def main(self):
        #self.comments()
        self.scroll()

if __name__ == '__main__':
    action = Action()
    action.main()