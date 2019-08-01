from dealer import dealerlogin
cookie = dealerlogin.login()
f = open('CookieForLr.dat','w',encoding='utf-8')
f.write('cookie'+'\n'+cookie+'\n')
f.close()