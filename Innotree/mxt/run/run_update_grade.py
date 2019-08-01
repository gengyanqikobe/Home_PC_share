import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")

from Innotree.mxt.db_sql.update_grade import update_grade

corp_name = input("请输入你要修改评分的企业名称：")
update_grade(corp_name)

#   testaccount10071的公司