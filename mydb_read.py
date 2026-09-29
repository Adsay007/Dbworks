import mysql.connector

con=mysql.connector.connect(user="root",password="12345",host="localhost",database="school_db")

c=con.cursor()

query = "select * from student"

c.execute(query)

records=c.fetchall()

if records:
    for row in records:
     print(row)
else:
   print ("No record Found")

c.close()
con.close()