#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:28:55 2019

@author: student
"""

from ageexception import AgeException

for i in range(3):
    try:
        id=int(input("Enter ID"))
        
        nm=input("Enter Name")
        
        age=int(input("Enter Age"))
        
        if age < 18 or age > 60:
            raise AgeException("Age should be in between 18 and 60")
            
        print("You entered ",id,nm,age,sep=" ")
        break
    
    except AgeException as e:
        print("In Age exception block")
        print(e)