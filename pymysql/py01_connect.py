import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="root",password="root",database="jianshenfanggl",charset="utf8")

cursor = conn.cursor()

cursor.execute("insert into qicai(id) VALUES(100)")

res = cursor.fetchmany(2)
print(conn.affected_rows())
conn.commit()

cursor.close()
conn.close()