#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:48:46 2019

@author: student
"""

import sqlite3
import sys
db=sqlite3.connect('mydb2.db')
if db!=None:
    print("Connected")
else:
    print("Not Connected")

cursor=db.cursor()    

def displayallDept():
    cursor.execute("select * from department")
    for r in cursor.fetchall():
        print(str(r[0])+","+str(r[1])+","+str(r[2])+","+str(r[3]))
    
def insertdept():
    dno=int(input("Enter department no : "))
    dname=input("Enter department name : ")
    loc=input("Enter the location : ")
    noe=input("Enter Employee numbers : ") 
    cursor.execute('''INSERT INTO department VALUES(?,?,?,?)''',(dno,dname,loc,noe))
    
    db.commit()

def deldept():
     dno=int(input("Enter department no: "))
     cursor.execute("delete from department where dno=?",(dno,))
     db.commit()
     
def updatedept():
    dno=int(input("Enter department no :"))
    cursor.execute("select * from department where dno=?",(dno,))
    r=cursor.fetchall()
    if len(r)!=0:
        ch=input("Do you want to change department name,location or employee no d/l/e")
        if ch=="d":
            dname=input("Enter new department name: ")
            cursor.execute("update department set dname=? where dno=?",(dname,dno,))
        elif ch=="l":
            loc=input("Enter the location")
            cursor.execute("update department set loc=? where dno=?",(loc,dno,))
        elif ch=="e":
            noe=int(input("Enter the new number of employees: "))
            cursor.execute("update department set noe=? where dno=?",(noe,dno,))
        db.commit()
       
    else:
        print("Not Found")
            
    
def diplayDept():
    dno=int(input("Enter the department number: "))
    cursor.execute("select * from department where dno=?",(dno,))
    for r in cursor.fetchall():
        print(str(r[0])+","+str(r[1])+","+str(r[2])+","+str(r[3]))
    
def displayloc():
    s=input("Enter the string you want to match")
    cursor.execute("select * from department where loc like ?",("%"+s+"%",))
    for r in cursor.fetchall():
        print(str(r[0])+","+str(r[1])+","+str(r[2])+","+str(r[3]))
    
    
    
    
choice=0
while choice!=7:
    print("1. Insert Data ")    
    print("2. Delete Data ")    
    print("3. Update Data")    
    print("4. Display All ")    
    print("5. Display by Department ")    
    print("6. Display department of location which conatins particular string")
    print("7. Exit")    
    choice=int(input("enter your choice"))
    if choice==1:
        insertdept()
    elif choice==2:
        deldept()
    elif choice==3:
        updatedept()
    elif choice==4:
        displayallDept()
    elif choice==5:
         diplayDept()
        
    elif choice==6:
        displayloc()
    elif choice==7:
        sys.exit(0)
    