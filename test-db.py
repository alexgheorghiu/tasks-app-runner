#!/usr/bin/python3
import os 
import pymysql

# Database connection parameters - update as needed
DB_USER = "dbmasteruser"
DB_PSWD = "+0H`2WV;Kw;%zWw8idz*r_6O,RORcZc7"
DB_NAME = "task_logger"
DB_HOST = "ls-3673dc7c4f0c9df0f4149d5deead6724b068ca4e.cn60uuew64vb.us-west-2.rds.amazonaws.com"

print("Content-type: text/html\n")
print("DB_USER=", DB_USER)
#print("DB_PSWD=", DB_PSWD)
print("DB_NAME=", DB_NAME)
print("DB_HOST=", DB_HOST)

try:
    db = pymysql.connect(
        host=DB_HOST, 
        user=DB_USER, 
        password=DB_PSWD, 
        database="mysql", 
        cursorclass=pymysql.cursors.DictCursor,
    ) 

    cursor = db.cursor() 
    cursor.execute("SHOW DATABASES") 
    
    print("Setup Successful")
except Exception as e:
    print("Setup unsuccessful.", e)