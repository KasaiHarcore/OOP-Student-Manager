import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
global ttdb
ttdb = mysql.connector.connect(host="localhost",user="DKtahuio",passwd="thanhdat4856",database="hocsinh")

ttcursor = ttdb.cursor()
ttcursor.execute("Select * from slist")
global thongtin
thongtin = ttcursor.fetchall()

import smtplib
import csv
import sys
import time
import os
global listStd
listStd = ["Nguyen Thanh Dat", "Nguyen Minh Quan" , "Nguyen Nhat Huy", " Le Dinh Duong","Tan Hoang Nam"]
x = "#" * 30
y = "=" * 28
global bye
bye = "\n {}\n# {} #\n# ========> pYE pyE <========= #\n# {} #\n {}".format(x, y, y, x)
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
   menu()
def menu():
    print("""
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------""")
    print(time.strftime("%c")) 
    print("HIIIII!!!!")
    print("This is what i can do and learn in 1 month ^^")
    print("Made by Datdeptraoi :>")
    print("""
1: Show Student.             
2: Edit Student.
3: Sort Student.
4: Send Alert.
5: Exit. """)  
    choice = input("Please enter your choice:")
    if choice == "1":
        Studentteam()
    elif choice == "2":
        Editting()
    elif choice == "3":
        Sort()
    elif choice == "4":
    	Alert()
    elif choice == "5":
        exit()
    else:
        print("You must only select either 1 to 5.")
        print("Please try again.")
        menu()





def Studentteam():
    print("""
1:Student list.
2:Student Infomation.
3:Return to mainmenu.""")
    choice = input("Please Select An Above Option:")
    if choice == "1":
        List()
    elif choice == "2":
        Info()
    elif choice == "3":
        menu()
    else:
        print("You must only select either 1 to 3.")
        print("Please try again.")
        Studentteam()

def List():
    print("List Students\n")  
    for students in listStd:
        print("=>{}".format(students))
    Studentteam()

def Info():
    for i in thongtin:
        print(i)
    Studentteam()





def Editting():
    print("""
1: Add Student.
2: Delete Student.
3: Edit Stu Info.
4: Return to mainmenu.""")
    choice = input("Chosse next decision:")
    if choice == "1":
        Adding()
    elif choice == "2":
        Deleting()
    elif choice == "3":
        Change()
    elif choice == "4":
         menu()
    else:
        print("You must only select either 1 to 4.")
        print("Please try again.")
        Editting()

def Adding():
    cursor = ttdb.cursor()
    id = input("New Student ID =")
    name = input("New Student Name =")
    age = input("New Student Age =")
    address = input("New Student Address =")
    email = input("New Student Email =")
    gpa = input("New Student GPA =")
    sql_insert_query = "insert into slist (ID, Name, Age, Address, Email, GPA) Value (%r, %r, %r, %r, %r, %r)"%(id,name,age,address,email,gpa)
    cursor.execute(sql_insert_query)
    ttdb.commit()
    print ("Adding successfully into slist table")
    Editting()

def Deleting():
    cursor = ttdb.cursor()
    print ("Records before deleting single record from student table")
    sql_select_query = """select * from slist"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    for record in records :
        print (record)
    id = input("Delete from slist where ID = ")
    sql_Delete_query = "Delete from slist where ID = %s" %id    
    cursor.execute(sql_Delete_query)
    ttdb.commit()
    print ("\nStudent remove successfully ")
    print("\nTotal records from student table after remove single record\n ")
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    Editting()

def Change():
    Change = ttdb.cursor()
    print("Write Student ID need to change:")
    id = input()
    print("If you don't want to change please rewrite the same")
    print("Change student Name:")
    name = input()
    print("Change student Age:")
    age = input ()
    print("Change student Address:")
    address = input ()
    print("Change student Email:")
    email = input ()
    print("Change student GPA:")
    gpa = input ()
    Changing = "Update slist set Name = %r , Age = %r , Address = %r , Email = %r, GPA = %r where ID = %r "%(name,age,address,email,gpa,id)
    Change.execute(Changing)
    ttdb.commit()
    record = Change.fetchone()
    print(record)
    print("Change Success")
    Editting()





def Sort():
    print("""
1:Sort by GPA.
2:Sort by name.
3:Return to mainmenu.""")    
    choice = input("Chosse next decision:")
    if choice == "1":
        GPAsort()
    elif choice == "2":
        namesort()
    elif choice == "3":
        menu()
    else:
        print("You must only select either 1 to 3.")
        print("Please try again.")
        Sort()
def GPAsort():
   dtb = ttdb.cursor()
   change = "SELECT * FROM slist ORDER BY GPA DESC"
   dtb.execute(change)
   myresult = dtb.fetchall()
   for r in myresult:
      print(r)
   print("Done")
   Sort()
def namesort():
   dtb = ttdb.cursor()
   change = "SELECT * FROM slist ORDER BY Name DESC"
   dtb.execute(change)
   myresult = dtb.fetchall()
   for r in myresult:
      print(r)
   print("Done")
   Sort()




def Alert():
    gmail_user = 'nguyendat4856@gmail.com'  
    gmail_password = 'dktahuio4856'

    sent_from = gmail_user  
    to = ('pubggodlike23@gmail.com')  
    subject = 'Alert Messange'  
    body = 'Hi! We send this to report your last exam GPA in lower than 5.5. Please spend time to study and learning to improve your skill. \n\n- Python'

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:  
        print('Something went wrong...')
        menu()



def exit():
    print(bye)
    sys.exit

menu()






















