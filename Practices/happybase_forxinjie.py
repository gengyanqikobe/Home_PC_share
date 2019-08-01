

#连接hbase，查数据增量
import time

import happybase
conn = happybase.Connection("10.64.0.114")

table = conn.table('CompanyAtomic:company_patent_source__expressSearch')
count = 0
for key in table.scan():
    count = count+1
    #print(key,value)
    print(count)
    #time.sleep(2)

print(count)