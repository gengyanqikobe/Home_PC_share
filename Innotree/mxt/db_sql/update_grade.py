import pymysql
from Innotree.mxt.read_config import Read_config

def update_grade(corp_name):

    db_host  = Read_config().get_DB('db_host')
    db_password = Read_config().get_DB('db_password')
    db_port = int(Read_config().get_DB('db_port'))
    db_name = Read_config().get_DB('db_name')
    #print(db_host,db_port,db_password,db_password)

    con = pymysql.connect(host = db_host,port = db_port,passwd = db_password,user = db_name,db = 'db_trustrader_certificate',charset = 'utf8')

    cursor = con.cursor(cursor = pymysql.cursors.DictCursor)

    sql_update = "UPDATE  `tb_cert_flow` set corp_grade = 790.00 where corp_name LIKE corp_name"


    cursor.execute(sql_update)
    #更新完了一定要commit，不然数据库中值没变
    con.commit()

    # se = "select * from `tb_cert_flow` where corp_name Like 'testaccount77%'"
    # cursor.execute(se)
    # tem = cursor.fetchall()#
    # print(tem)
    cursor.close()
    con.close()

#update_grade('testaccount10026的公司')