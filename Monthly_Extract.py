import sqlite3
import datetime

roll_no = int(input("Enter roll no of the student: "))
month = int(input("Enter the month in digits: "))
year = int(input("Enter Year: "))

def viewall(roll_no,month,year):
   Starting_date = datetime.date(year,month,1)
   Ending_date = datetime.date(year,month,30)
   connection = sqlite3.connect("college.db")
   Cursor = connection.cursor()
   Cursor.execute("SELECT * FROM attendance WHERE roll_no = ? and day > =? and day <= ? ",(roll_no,Starting_date,Ending_date))
   global data
   data = Cursor.fetchall()
def feedfile(data,roll_no,month):
   d={1:"January",2:"february",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December",}
   f = open(f"Details_of_student_of_roll_no: {roll_no}_for_the_month_of {d[month]}","w")
   for row in data:
      for element in row:
         f.write(str(element))
         f.write(",")
      f.write("\n")
   f.close()
viewall(roll_no,month,year)
feedfile(data,roll_no,month)
