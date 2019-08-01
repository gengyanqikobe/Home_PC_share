import configparser
conf = configparser.ConfigParser()
conf.add_section('login')
conf.set('login','name','gyq')
conf.set('login','password','gyq123')

conf.add_section('db')
conf.set('db','host','192.168.1.1')
conf.set('db','port','8888')
conf.set('db','username','name1')
conf.set('db','password','passowrd1')

conf.add_section('url')
conf.set('url','url','baidu.com')

conf.add_section('Email')
conf.set('Email','mail_host','stmp@163.com')
conf.set('Email','mail_port','25')
conf.set('Email','mail_user','gengyanqikobe@163.com')
conf.set('Email','mail_password','testpassowrd')
conf.set('Email','sender','gengyanqikobe@163.com')
conf.set('Email','receiver','1254804641@qq.com')
conf.set('Email','subject','关于通讯接口的测试报告')
conf.set('Email','content','你好，以下是通讯接口的测试报告，请查阅：')
conf.set('Email','testuser','耿艳奇')


with open('cofnig_lianxi.ini','w') as f:
    conf.write(f)


name = conf.get('login','name')
port = conf.get('db','port')
content = conf.get('Email','content')
print(name,port,content)