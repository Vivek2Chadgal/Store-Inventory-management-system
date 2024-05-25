import mysql.connector as my
mydb=my.connect(host="localhost",user="root",password="mysql")
mycursor=mydb.cursor()
mycursor.execute("create database stocks")
mydbs=my.connect(host="localhost",user="root",password="mysql",database="stocks")
myx=mydbs.cursor()
myx.execute("CREATE TABLE PRODUCTS(pcode integer primary key,pname char(20),pprice integer,pqty integer,pcat char(30));")
