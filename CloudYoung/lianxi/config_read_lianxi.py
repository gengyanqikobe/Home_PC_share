
import configparser
cf = configparser.ConfigParser()
cf.read('cofnig_lianxi.ini')
secs = cf.sections()#sections是组名称
print('secs is :',secs)

items = cf.items('login')
print(items)#得到sections里面的所有的键值对

opts = cf.options('login')
opts = cf.options('Email')#得到sections里面的键值
print('opts is :',opts)

name = cf.get('login','name')#返回为string类型值，要是想返回int类型则用getint
passowrd = cf.get('login','password')
print('login name is:',name,'\n login password is:',passowrd)

mail_user = cf.get('Email','mail_user')
print(mail_user)