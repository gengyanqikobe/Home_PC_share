import configparser
conf = configparser.ConfigParser()

conf.add_section('DATABASE')
conf.set('DATABASE','db_host','211.108.1.2')
conf.set('DATABASE','db_username','mysql')
conf.set('DATABASE','db_password','mima123')
conf.set('DATABASE','db_port','3306')

conf.add_section('EMAIL')
conf.set('EMAIL','mail_host','stmp@163.com')
conf.set('EMAIL','mail_port','25')
conf.set('EMAIL','mail_user','gengyanqikobe@163.com')
conf.set('EMAIL','mail_password','testpassowrd')
conf.set('EMAIL','sender','gengyanqikobe@163.com')
conf.set('EMAIL','receiver','1254804641@qq.com/1321188988@qq.com/test123.com',)
conf.set('EMAIL','subject','关于通讯接口的测试报告')
conf.set('EMAIL','content','你好，以下是通讯接口的测试报告，请查阅：')
conf.set('EMAIL','testuser','耿艳奇')
conf.set("EMAIL",'title','这是一次测试title')

conf.add_section("HTTP")
conf.set("HTTP",'baseurl','baidu.com')
conf.set("HTTP",'timeout','10')



with open('config.ini','w')as f:
    conf.write(f)