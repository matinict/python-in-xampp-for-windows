#!D:/python-3.6.2/python.exe 
print ("Content-Type: text/html\n")
import pymysql
 
db = pymysql.connect(host="localhost", user="root", passwd="", db="python_mysql")
 
cur = db.cursor()
 
cur.execute("SELECT * FROM authors")
 
row = cur.fetchall()
 
print (row[1])
