#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:21:55 2019

@author: student
"""

import sys
from account import *

def searchPosition(lst, aid):
    pos = 0
    for i in lst:
        if i.getId() == aid:
            return pos
        pos += 1
    else:
        return -1

def createAcc(lst):
    print('1. Savings')
    print('2. Current')
    ch = int(input('Enter the choice : '))
    if ch == 1:
        aid = int(input('Enter the accont Id : '))
        name = input('Enter the accont name : ')
        bal = int(input('Enter the accont balance : '))
        chno = int(input('Enter the accont checkbook no : '))
        s = Savings(aid, name, bal, chno)
        lst.append(s)
        return True
    elif ch == 2:
        aid = int(input('Enter the accont Id : '))
        name = input('Enter the accont name : ')
        bal = int(input('Enter the accont balance : '))
        creditno = int(input('Enter the Creditcard no : '))
        c = Current(aid, name, bal, creditno)
        lst.append(c)
        return True
    else:
        return False
def delAcc(lst):
    aid = int(input('Enter the accont Id to delete : '))
    pos = searchPosition(lst, aid)
    if pos != -1:
        lst.pop(pos)
        return True
    else:
        return False
    
def deposit(lst):
    aid = int(input('Enter the accont Id to delete : '))
    pos = searchPosition(lst, aid)
    if pos != -1:
        damt = float(input('Enter the ammount to deposit : '))
        lst[pos].deposit(damt)
        return True
    else:
        return False

def withdraw(lst):
    aid = int(input('Enter the accont Id to withdraw : '))
    pos = searchPosition(lst, aid)
    if pos != -1:
        wamt = float(input('Enter the ammount to be withdraw : '))
        if lst[pos].withdraw(wamt):
            return True
        else:
            return False
    else:
        return False
    

def transfer(lst):
    aid1 = int(input('Enter the accont Id to to transfer from : '))
    aid2 = int(input('Enter the accont Id to to transfer to : '))
    pos = 0
    id1 = False
    id2 = False
    for i in lst:
        if aid1 == i.getId():
            pos1 = pos
            id1 = True
        if aid2 == i.getId():
            pos2 = pos
            id2 = True
        pos += 1
    if id1 and id2:
        amt = float(input('Enter the ammount to Transfer : '))
        if lst[pos1].withdraw(amt):
            if lst[pos2].deposit(amt):
                return True
            else:
                lst[pos1].deposit(amt)
                return False
        else:
            return False

def display(lst):
    for i in lst:
        print(i)