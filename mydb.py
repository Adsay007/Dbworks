import mysql.connector
"""
con=mysql.connector.connect(user="root",password="12345",host="localhost")
print(con)

#cursor object -- for executing sql qureies
c=con.cursor()
query = "create database school_db"
c.execute(query)
print("Database File created")
c.close()
con.close()
"""

con=mysql.connector.connect(user="root",password="12345",host="localhost",database="school_db")
c=con.cursor()
query = ("create table student("
        "roll_no int not null primary key, "
        "name varchar(20) ,"
        "age int , "
        "place varchar(20), "
        "phone varchar(20), "
        "total_mark int)")
c.execute(query)
print("table Created ")