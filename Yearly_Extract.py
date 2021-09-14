import sqlite3
import datetime

roll_no = int(input("Enter roll no of the student: "))
year = int(input("Enter Year: "))

def viewall(roll_no,year):
   Starting_date = datetime.date(year,1,1)
   Ending_date = datetime.date(year,12,31)
   connection = sqlite3.connect("college.db")
   Cursor = connection.cursor()
   Cursor.execute("SELECT * FROM attendance WHERE roll_no = ? and day > =? and day <= ? ",(roll_no,Starting_date,Ending_date))
   global data
   data = Cursor.fetchall()
def feedfile(data,roll_no,year):
   f = open(f"Details_of_student_of_roll_no: {roll_no}_for_the_year_of {year}","w")
   for row in data:
      for element in row:
         f.write(str(element))
         f.write(",")
      f.write("\n")
   f.close()
viewall(roll_no,year)
feedfile(data,roll_no,year)
