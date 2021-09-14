import sqlite3
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

sql_command = """
CREATE TABLE attendance (
Roll_No INTEGER,
First_Name Varchar(20),
Last_Name Varchar(30),
Day DATE,
status CHAR(1) ) ;"""
cursor.execute(sql_command)
