#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:10:05 2019

@author: student
"""
from BankClasses import *
from BankFunctions import * 

import sys

plist=[]
choice=0
while choice !=8:
    print("1. Add account " )
    print("2. Withdraw amount ")
    print("3. Deposit ")
    print("4. Transfer amount")
    print("5. Check Balance")
    print("6. Delete Account")
    print("7. Display Details")
    print("8. Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        
        ans=input("Choose type of account you want to create? s/c ")
        if ans=="s":
            addsaving(plist)
            print("Added Successfully")
            
        else:
            addcurrent(plist)
            print("Added Successfully")
            
            
            
        
    elif choice==2:
        withdrawfun(plist)

        
    elif choice==3:
        depos(plist)
    elif choice==4:
        pass
    elif choice==5:
        
        pos=int(input("Enter the Id for Balance : "))
        
        ans=SearchById(plist,pos)
        if ans!= -1:
            
            a=plist[ans]
            print(a.getBal())
        else:
            print("Id not Found")
    
    elif choice==6:
        pass
    elif choice==7:
        DisplayData(plist)
    else:
        sys.exit(0)
