# step1 : importing mysql.connector

import mysql.connector

#step2 : establishing a connection with mysql

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password@123',
    auth_plugin='mysql_native_password'
)

# step3 : create a cursor object (like mediator between python and mysql)

cursor = db.cursor()                    # creating cursor object

sql = "select version()"                # sql is variablenormal created by user with string object(not a sql query now)
cursor.execute(sql)                     # execute() used to execute sql query given in sql variable
data = cursor.fetchone()                # fetchone() is used to fetch data from mysql, if we dont want to fetch anything, dont write this code
print(data)
db.close()                              # terminating the connection