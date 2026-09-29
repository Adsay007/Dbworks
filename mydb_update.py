import mysql.connector

con=mysql.connector.connect(user="root",password="12345",host="localhost",database="school_db")

c=con.cursor()


query="update student set name=%s where roll_no=%s"

data=("amal",101)

c.execute(query,data)

con.commit()

if c.rowcount>0:
    print("Record Updated")
else:
    print("No Data Found")