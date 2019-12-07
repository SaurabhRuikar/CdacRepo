#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 08:58:19 2019

@author: student
"""
from pymongo import MongoClient
import sys
client=MongoClient('localhost:27017')

print('connection done')

db=client.EmployeeData

def insert():
    try:
        employeeid=int(input('Enter employee id : '))
        employeeName=input('Enter Name : ')
        employeeAge=int(input('Enter age : '))
        employeeCountry=input('Enter Country : ')
        db.Employees.insert_one(
                {
                "id":employeeid,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry                
                }
                )
        print('Inserted successfully')
    except Exception as e:
        print(str(e))
    
def read():
    try:
        r=db.Employees.find()
        for i in r:
            print(i)
    except Exception as e:
        print(str(e))


def update():
    try:
        employeeid=int(input('Enter employee id to be updated : '))
        employeeName=input('Enter Name to be updated : ')
        employeeAge=int(input('Enter age to be updated : '))
        employeeCountry=input('Enter Country to be updated : ')
        db.Employees.update_one(
                
                {'id':employeeid},
                {
                "$set":{
                "name":employeeName,
                'age':employeeAge,
                "country":employeeCountry                
                }
                }
                )
            
        print('\n Updated successfully')
    
    except Exception as e:
        print(str(e))
    



def delete():
    try:
        employeeid=int(input("\n Enter Employee id to Delete : "))
        db.Employees.delete_many({'id':employeeid})
        print('\n Deletion Successful \n')
    except Exception as e:
        print(str(e))



choice=0


while(1):
    choice=input('\n Select \n 1. Insert \n 2. Update \n 3. Read \n 4. Delete \n 5. Exit \n')
    
    if choice=='1':
        insert()
    elif choice=='2':
        update()
    elif choice=='3':
        read()
    elif choice=='4':
        delete()
    else:
        sys.exit(0)
    
    
    
    