from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.taobao.com')
#一开始原有的cookie
print(browser.get_cookies())
#手动增加cookie后
browser.add_cookie({'name': 'kkk', 'value': 'wHACFTBcN1oCAW/BKPaY4zBl', 'path': '/', 'domain': '.taobao.com', 'expiry': 2182318274, 'secure': False, 'httpOnly': False})
print(browser.get_cookies())
#删除所有cookie
browser.delete_all_cookies()
print(browser.get_cookies())