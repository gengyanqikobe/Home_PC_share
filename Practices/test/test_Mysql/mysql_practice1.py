


import  pymysql
from Innotree.mxt.read_config import Read_config


#测试随机从数据库中取数据

def test_random():

    #config里面取出要用的数据库信息

    host = Read_config().get_DB('db_host')
    password = Read_config().get_DB('db_password')
    port = int(Read_config().get_DB('db_port'))         #端口号必须是整数
    username = Read_config().get_DB('db_name')

    #注意最后的charset是utf8，不是utf-8
    conn = pymysql.connect(host = host,passwd = password,port = port,user = username,db = 'db_trustrader_certificate',charset = 'utf8')
    #con = pymysql.connect(host = db_host,port = db_port,passwd = db_password,user = db_name,db = 'db_trustrader_certificate',charset = 'utf8')


    #cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)  #以字典形式返回，带有key
    cursor = conn.cursor()                              #默认元组方式返回，只有值

    sql_get_random_value = "SELECT corp_name FROM `tb_cert_flow` ORDER BY rand() LIMIT 10"

    cursor.execute(sql_get_random_value)
    value_temp = cursor.fetchall()          #一定要用fetchall来接受一下去的值
    #print(type(value_temp))
    cursor.close()
    conn.close()
    return value_temp


tuple_corp_name = test_random()
print(len(tuple_corp_name))
total = ()
for i in tuple_corp_name:       #元组相加
    total = total +i         #输出公司名字
print(total)