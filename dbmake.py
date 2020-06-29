import pymysql
import datetime
connect = pymysql.connect(host='localhost',user='root',password='123',db='rasa',charset='utf8',autocommit=True)
cursor = connect.cursor(pymysql.cursors.DictCursor)

sql = """insert into info values("이진수",25,"남","960417-1157610","jins@naver.com", "DEFAULT","DEFAULT");"""
cursor.execute(sql)
#d = datetime.date.today()
#now = datetime.timedelta(days=1)
#for i in range(100):
#    d = d + now
#    sql ="""insert into SCHEDULE_DERMA values("{}","N","N","N","N","N","N","N","N");""".format(str(d))
#    cursor.execute(sql)
