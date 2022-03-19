import mysql.connector as mysql

connection = mysql.connect(user='root',password='ayush123')

cursor = connection.cursor()
cursor.execute("show databases")

for i in cursor:
	print(i)

connection.close()