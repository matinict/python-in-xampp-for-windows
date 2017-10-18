#!D:/python-3.6.2/python.exe 
print ("Content-Type: text/html\n")
import pymysql.cursors  
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                            
                             db='pymysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try: 
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT email, password FROM users "        
        # Execute query
        cursor.execute(sql)        
        print ("cursor.description: ", cursor.description) 
        print() 
        for row in cursor:
            print(row)            
finally:
    connection.close()
