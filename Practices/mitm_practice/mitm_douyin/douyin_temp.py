__author__ = 'KOBE'





from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


devices_caps = {
    "platformName": "Android",
    "deviceName": "Redmi 4X",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    "platformVersion": "6.0.1",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server,devices_caps)
#driver.implicitly_wait(15)
start_x = 366
start_y = 948
distance = 600


#sleep(7)
"""
try:
    driver.find_element_by_id('y7').click()
except Exception as e:
    print('没有定位到,我知道了')
"""
driver.swipe(start_x,start_y,start_x,start_y-distance,duration=300)
print("begin")
locator = (By.ID,"y7")
e = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
e.click()
print("end")

sleep(1)
driver.swipe(start_x,start_y,start_x,start_y-distance,duration=300)

sleep(2)
#进入搜索页面
driver.find_element_by_id('com.ss.android.ugc.aweme:id/azj').click()
sleep(10)
#搜索美女
driver.find_element_by_id('com.ss.android.ugc.aweme:id/aar').click()
driver.find_element_by_id('com.ss.android.ugc.aweme:id/aar').send_keys('美女')

sleep(2)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/dis').click()
sleep(5)
#切换到视频页
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView').click()
sleep(3)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView').click()
sleep(3)
driver.swipe(start_x,start_y,start_x,start_y-distance,duration=300)
sleep(5)
driver.swipe(start_x,start_y,start_x,start_y-distance,duration=300)