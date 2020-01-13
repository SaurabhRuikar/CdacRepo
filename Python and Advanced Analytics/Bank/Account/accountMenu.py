#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:33:04 2019

@author: student
"""
import sys
from account import *
from accountFunctions import *
        
acclst = []
ch = 0
while ch != 7:
    print('-----------------------')
    print('1. Add Account')
    print('2. Delete Account')
    print('3. Deposit')
    print('4. Withdraw')
    print('5. Transfer')
    print('6. Display')
    print('7. Exit')
    print('-----------------------')
    ch = int(input('Enter the choice : '))
    if ch == 1:
        if createAcc(acclst):
            print('Account Created')
        else:
            print('Account not Created')
            
    elif ch == 2:
        if delAcc(acclst):
            print("Account Deleted")
        else:
            print("Account  not Deleted")
            
    elif ch == 3:
        if deposit(acclst):
            print('Ampunt Deposited')
        else:
            print('Ampunt not Deposited')
            
    elif ch == 4:
        if withdraw(acclst):
            print('Withdraw successfully')
        else:
            print('Insufficient Balance')
    
    elif ch == 5:
        if transfer(acclst):
            print('Transfered Successfully')
        else:
            print('Failed to Transfer')
        
    elif ch == 6:
        display(acclst)
        
    else:
        sys.exit(0)