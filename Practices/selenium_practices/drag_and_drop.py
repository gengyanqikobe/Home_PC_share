from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
#切换到元素所在frame
browser.switch_to.frame('iframeResult')
#起点
start = browser.find_element_by_id('draggable')
#终点
end = browser.find_element_by_id('droppable')

action = ActionChains(browser)
action.drag_and_drop(start,end)
#执行
action.perform()
time.sleep(3)
#browser.close()
