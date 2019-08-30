import pymysql
from datetime import datetime
conn=pymysql.connect(host='sql12.freemysqlhosting.net',user='sql12303463',password='qln7hJ7jQX',db='sql12303463')
a1=conn.cursor()
t=['74','prethiv','10:15','290819']
sql="INSERT INTO inat (id, name, intime, date) VALUES (%s, %s, %s, %s)"
#sql="SELECT * FROM inat"
a1.execute(sql,t)
#data=a1.fetchall()
#for i in data:
#    print(i)
conn.commit()
print("entry put")
