import configparser

conf = configparser.ConfigParser()

conf.add_section("DB")
conf.set('DB','db_host','10.64.0.111')
conf.set('DB','db_name','root')
conf.set('DB','db_port','3306')
conf.set('DB','db_password','hcIWtm^}$#=eZ|u')




with open('config.ini','w')as f:
    conf.write(f)