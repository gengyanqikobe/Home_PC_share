import configparser
#参考资料
# https://my.oschina.net/u/3041656/blog/793467

#  实例化configParser对象
cf = configparser.ConfigParser()

#读取配置文件
cf.read('cofnig_lianxi.ini')

def getEmailUser():
    value = cf.get('Email','mail_user')
    return value
def getEmailPassword():
    value = cf.get('Email','mail_password')
    return value

mail_user = getEmailUser()
print('邮箱的用户名是：',mail_user)
mail_password = getEmailPassword()
print('邮箱的密码是：',mail_password)

