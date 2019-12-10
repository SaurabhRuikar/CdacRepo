#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:50:58 2019

@author: student
"""

from pymongo import MongoClient
import sys
client=MongoClient('localhost:27017')

print('connection done')

db=client.Product


def insert():
    try:
        pid=int(input('Enter Product id : '))
        pName=input('Enter Product Name : ')
        pquantity=int(input('Enter Product Quantity : '))
        price=int(input('Enter Price : '))
        db.product.insert_one(
                {
                "id":pid,
                "name":pName,
                "pquantity":pquantity,
                "price":price                
                }
                )
        print('Inserted successfully')
    except Exception as e:
        print(str(e))


def read():
    try:
        r=db.product.find()
        for i in r:
            print(i)
    except Exception as e:
        print(str(e))



def delete():
    try:
        pid=int(input("\n Enter Product id to Delete : "))
        db.product.delete_many({'id':pid})
        print('\n Deletion Successful \n')
    except Exception as e:
        print(str(e))


def update():
    try:
        pid=int(input('Enter Product id : '))
        pName=input('Enter Product Name : ')
        pquantity=int(input('Enter Product Quantity : '))
        price=int(input('Enter Price : '))
        db.product.update_one(
                   
                    {'id':pid},
                    {
                    "$set":{
                    "name":pName,
                    'pquantity':pquantity,
                    "price":price                
                    }
                    }
                    )
                
        print('\n Updated successfully')
    
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