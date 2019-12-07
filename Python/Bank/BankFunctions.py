#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:09:53 2019

@author: student
"""
from BankClasses import *
lst=[]
str=""
def addsaving(lst):
    id=int(input("Enter the ID"))
    name=input("Enter the name")
    balance=int(input("Enter the amount you want to add"))
    chkno=input("Enter the Chequebook Number")
    s=SavingAcc(id,name,balance,chkno)
    lst.append(s)

def addcurrent(lst):
    id=int(input("Enter the ID"))
    name=input("Enter the name")
    balance=int(input("Enter the amount you want to add"))
    cred=input("Enter the creditcard number")
    c=CurrentAcc(id,name,balance,cred)
    lst.append(c)
    
    
def DisplayData(lst):
    for p in lst:
        print(p)
        print("-----------------------")    
        
     
def SearchById(lst,id):
    
    count=0
    for i in lst:
        if i.getId()==id:
            return count

        count=count + 1

    else:
        return -1
        
    
def withdrawfun(lst):
    pos=int(input("Enter Your Acc Id : "))
    ans=SearchById(lst,pos)
    if ans!= -1:
        amt=int(input("enter amount to withdraw"))
        lst[ans].withdraw(amt)
    else:
        print("id not found")
        
def depos(lst):
    pos=int(input("Enter Your Acc Id : "))
    ans=SearchById(lst,pos)
    if ans!= -1:
        amt=int(input("Enter amount to be added"))
        lst[ans].depos(amt)
        
            
            
    else:
        print("id not found")
   
 
    

    
    
    
    
    
    
    
    