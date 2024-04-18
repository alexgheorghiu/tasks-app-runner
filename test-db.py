#!/usr/bin/python3
import os 
import pymysql

# Database connection parameters - update as needed
DB_USER = os.getenv("DB_USER") or "task_logger"
DB_PSWD = os.getenv("DB_PSWD") or "task_logger"
DB_NAME = os.getenv("DB_NAME") or "task_logger"
DB_HOST = os.getenv("DB_HOST") or "localhost"

print("Content-type: text/html\n")

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