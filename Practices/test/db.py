#数据库测试

import pymysql
from Innotree.mxt.read_config import Read_config
import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")


#获取数据库信息
db_host = Read_config().get_DB('db_host')
db_name = Read_config().get_DB('db_name')
db_password = Read_config().get_DB('db_password')
#端口号需要是整数，而不是str
db_port = int(Read_config().get_DB('db_port'))
print(db_host,db_name,db_password,db_port)

con = pymysql.connect(host = db_host,user = db_name,port = db_port,passwd = db_password,db = 'db_trustrader_account' )
cursor = con.cursor(cursor = pymysql.cursors.DictCursor)

sql_testaccout = "SELECT * FROM `tb_platform_user`where user_name LIKE 'testaccount%'"
sql_order_by = "SELECT * FROM `tb_platform_user` WHERE user_name LIKE 'test%'ORDER BY user_phone DESC limit 20"

sql_exist  = "SELECT user_name FROM `tb_platform_user`where user_email = 'gengyanqikobe@163.com'"

sql_update = "UPDATE  `tb_cert_flow` set corp_grade = '778' where corp_name LIKE 'testaccount77%'"

cursor.execute(sql_update)


# cursor.execute("SELECT * FROM `tb_platform_user`")
# temp1 = cursor.fetchall()
#
# with open('test.txt','w')as f:
#     for i in temp1:
#         for j in i:
#             f.write(str(j)+' ')
#         f.write('\n')


   # f.write(temp1)


# temp = cursor.fetchall()
#
# if len(temp) == 0:
#     print('null')
# else:
#     for i in temp:
#         print(i)

cursor.close()
con.close()