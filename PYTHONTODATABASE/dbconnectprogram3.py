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

# to insert value into table
try:
    sql = "insert into movie values(101,'lifeofpies','2007',5)"
    # executing the code with cursor object
    cursor.execute(sql)
    print("row inserted")
    # we need to commit to update the db
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()                      # if exception occur, go to previous state, ie, no partial entry of data.

# closing db
db.close()

