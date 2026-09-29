import mysql.connector

con=mysql.connector.connect(user="root",password="12345",host="localhost",database="school_db")

c=con.cursor()

query="select * from student where roll_no=%s"

data= (101,)

c. execute (query, data)

record=c.fetchone()

if record:
    print(record)
else:
    print("No Record Found")

c. close ()
con. close()