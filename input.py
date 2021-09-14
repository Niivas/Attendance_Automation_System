import sqlite3
import datetime

def insert(roll_no,first_name,last_name,day,status):
   connection = sqlite3.connect("college.db")
   Cursor = connection.cursor()
   Cursor.execute("INSERT INTO attendance VALUES (?,?,?,?,?)",(roll_no,first_name,last_name,day,status))
   connection.commit()
   connection.close()
def parse(csv_file_name):
   table = []
   with open(csv_file_name,"r") as file:
      for line in file:
         columns = line.rstrip().split(",")
         table.append(columns)
      return table
def feeddb(table):
   for i in table:
      a= int(i[0])
      b= str(i[1])
      c= str(i[2])
      d = (i[3].strip()).split("-")
      day = int(d[0])
      month = int(d[1])
      year = int(d[2])
      d1 = datetime.date(year,month,day)
      e= str(i[4])
      insert(a,b,c,d1,e)
feeddb(parse("students.csv"))
