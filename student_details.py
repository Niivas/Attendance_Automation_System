import sqlite3
roll_no = int(input("Enter roll no of student: "))

def viewall(roll_no):
   connection = sqlite3.connect("college.db")
   Cursor = connection.cursor()
   Cursor.execute("SELECT * FROM attendance WHERE roll_no = ? ",(roll_no,))
   global data
   data= Cursor.fetchall()

def feedfile(data,roll_no):
   f = open(f"Details_of_student_of_roll_no: {roll_no}","w")
   for row in data:
      for element in row:
         f.write(str(element))
         f.write(",")
      f.write("\n")
   f.close()
viewall(roll_no)
feedfile(data,roll_no)
