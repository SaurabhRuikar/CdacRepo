#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:19:54 2019

@author: student
"""

import sys

import numpy as np


def createArange():
    r1=int(input("Enter the number of rows for matrix A "))
    c1=int(input("Enter the number of column for matrix A "))
    m1=r1*c1
    a=np.arange(m1).reshape(r1,c1)
    print(a)

    r2=int(input("Enter the number of rows for matrix B "))
    c2=int(input("Enter the number of column for matrix B "))
    m2=r2*c2
    b=np.arange(m2).reshape(r2,c2)
    print(b)
    
    print("Shape of Matrix A is : ")
    print(a.shape)
    print("Shape of Matrix B is : ")
    print(b.shape)
    
    
    if c1==r2:
        print(np.dot(a,b))
    else:
        print("Can't perform multiplication since rows and columns do not match")


def createRand():
    r1=int(input("Enter the number of rows for matrix C "))
    c1=int(input("Enter the number of column for matrix C "))
    m1=r1*c1
    
    c=np.random.randn(m1).reshape(r1,c1)
    print(c)
    
    r2=int(input("Enter the number of rows for matrix A "))
    c2=int(input("Enter the number of column for matrix A "))
    m2=r2*c2
    a=np.arange(m2).reshape(r2,c2)
    print(a)
    
    if r1==r2 and c1==c2:
        print('Addition is ')
        print(a+c)
        print()
        print('Subtraction is ')
        print(a-c)
        print()
        print('Multiplication is ')
        print(a*c)
        
        
    else:
        print("Row and columns do not match so can't perform operations")
   

choice=0
while choice!=3:
    print("1. Create Matrix A and B ")
    print("2. Create Random Matrix C ")
    print("3. Exit ")
    
    choice=int(input("Enter your choice : "))
    

    if choice==1:
        createArange()
    elif choice==2:
        createRand()
    else:
        sys.exit(0)




