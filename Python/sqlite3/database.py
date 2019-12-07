#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:27:14 2019

@author: student
"""

import sqlite3
import sys
db=sqlite3.connect('mydb1.db')  #Connecting to database
if db!=None:
    print("Connection done")
else:
    print("Connection not done")    


cursor=db.cursor()  #cursor generate some RAM for data coming from database

def displayAll():
    cursor.execute("select * from mytable")
    for row in cursor.fetchall():#It returns list of tuple eg.[(10,'aaa'354),(20,'abc'222)]
        print(str(row[0])+","+str(row[1])+","+str(row[2]))
        #print(row)#Tuple
        
        
def insertrec():
    id=int(input("Enter id"))
    name=input("Enter the name")
    sal=int(input("Enter salary"))
    cursor.execute('''INSERT INTO mytable VALUES(?,?,?)''',(id,name,sal))        
    #cursor.execute('''INSERT INTO myatable VLUES(:id,:name,:sal)''',(id,name,sal)) for oracle :id indicates placeholders
    db.commit()
    
def deleterec():
    id=int(input("Enter id to be deleted"))
    cursor.execute("delete from mytable where id=?",(id,))
    #after id , comma is given because typle is size of 1    

def update():
    id=int(input("Enter id to be updated"))
    sal=int(input("Enter the salary"))
    cursor.execute("update mytable set sal=? where id=?",(sal,id,))
    db.commit()

def displayID():
    id=int(input("Enter id to be searched"))
    cursor.execute("select * from mytable where id=?",(id,))
    for row in cursor:
        print(str(row[0])+","+str(row[1])+","+str(row[2]))
    

#ans="y"
choice=0
while choice!=6:
    print("1. Insert Data ")    
    print("2. Delete Data ")    
    print("3. Modify Data")    
    print("4. Display All ")    
    print("5. Display by Id ")    
    print("6. Exit ")
    choice=int(input("Enter the choice"))
    if choice==1:
        insertrec()
    elif choice==2:
        deleterec()
    elif choice==3:
        update()
    elif choice==4:
        displayAll()
    elif choice==5:
        displayID()
        
    elif choice==6:
        sys.exit(0)
