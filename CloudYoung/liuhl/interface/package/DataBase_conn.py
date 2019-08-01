# -*- coding:utf-8 -*-

import pymysql
import configparser
import csv
from os.path import abspath,dirname

'''获取配置文件内信息'''
file_path = dirname(abspath(__file__)) + '/conf.ini'
config = configparser.ConfigParser()
config.read(file_path)
config = eval(config.get('DataBase', 'config'))

'''连接数据库'''
connect = pymysql.connect(**config)

# '''从cvs文件中读取sql'''
# csv_s = dirname(abspath(__file__)) + '/Test_data.csv'
#
# with open(csv_s, 'r', encoding='utf-8') as r:
#     read_r = csv.reader(r)
#     row = [row for row in read_r]
#     print(row)
#     r.close()
#
# with open(csv_s, 'r', encoding='utf-8') as r:
#     read_r = csv.reader(r)
#     for i, rows in enumerate(read_r):
#         print(i, rows)
#         if i == 1:
#             row = rows[1]
#             print(row)
#     r.close()

try:
    with connect.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        '''从ini文件获取信息'''
        config = configparser.ConfigParser()
        config.read(file_path)
        sql = config.get('SQL', 'sql')
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            print(i)

finally:
    connect.close()