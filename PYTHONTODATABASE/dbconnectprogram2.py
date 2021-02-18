# step1 : importing mysql.connector

import mysql.connector

#step2 : establishing a connection with mysql

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password@123',
    auth_plugin='mysql_native_password',
    database='pythondecember'
)

# step3 : create a cursor object (like mediator between python and mysql)

cursor = db.cursor()

sql = "create table movie(movie_id int,movie_name varchar(50),year varchar(15),review int)"

cursor.execute(sql)
# nothing to fetch from db because we are creating a table
print("Movie table created in database pythondecember")
db.close
