


#访问hive，统计条数

from pyhive import hive

conn = hive.Connection(host='10.64.0.113',port=10000,username='duyaping',password='duyaping',database='spider',auth='CUSTOM')
'''
cursor = conn.cursor()

sql = 'SELECT count(0) FROM `app_base_info__wandoujia`'

cursor.execute(sql)
'''

conn.close()