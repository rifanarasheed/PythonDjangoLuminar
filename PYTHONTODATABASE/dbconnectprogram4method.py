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

def get_data():
    # step3 : create a cursor object (like mediator between python and mysql)
    cursor = db.cursor()
    sql = "select * from movie"
    cursor.execute(sql)
    movies = cursor.fetchall()
    yield movies                         # yeild will loading and returning row one by one(if return given, all together will be returned)

movies = get_data()
print(movies)

db.close
