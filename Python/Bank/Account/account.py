#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:08:38 2019

@author: student
"""

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, aid, name, balance):
        self.__aid = aid
        self.__name = name
        self.__balance = balance
    
    def getId(self):
        return self.__aid
    
    def getName(self):
        return self.__name
    
    def getBalance(self):
        return self.__balance
    
    def setId(self, aid):
        self.__aid = aid
    
    def setName(self, name):
        self.__name = name
    
    def setBalance(self, bal):
        self.__balance = bal
    
    def __str__(self):
        return 'Id : '+str(self.__aid)+' Name : '+str(self.__name)+'  Balance : '+str(self.__balance)
    
    def withdraw(self, amt):
        if self.__balance < amt or self.__balance < 5000 or self.__balance - amt < 5000:
            return False
        else:
            self.__balance -= amt
            return True
    
    def deposit(self, damt):
        self.__balance += damt
        return True
    
    def checkBalance(self):
        pass
    

class Savings(Account):
    
    intrest_rate = 0.08
    
    def __init__(self, aid, name, balance, chno):
        Account.__init__(self, aid, name, balance)
        self.__chno = chno
        
    def getChno(self):
        return self.__chno
    
    def setChno(self, chno):
        self.__chno = chno
    
    def __str__(self):
        return Account.__str__(self)+' Check Book No : '+str(self.__chno)
    
    def checkBalance(self):
        return self.getBalance() + self.getBalance() * Savings.intrest_rate

class Current(Account):
    
    max_tran = 3
    def __init__(self, aid, name, balance, creditno):
        Account.__init__(self, aid, name, creditno)
        self.__tno = 0
        self.__creditno =creditno
        
    def getTno(self):
        return self.__tno
    
    def setTno(self, tno):
        self.__tno = tno
        
    def getCreditNo(self):
        return self.__creditno
    
    def setCreditNo(self, chno):
        self.__creditno = creditno
        
    def __str__(self):
        return Account.__str__(self)+' No of Transaction  : '+str(self.__tno) +'Credit Card No : '+str(self.__creditno)
    
    def checkBalance(self):
        return self.getBalance()
    
    
    
    
    
    
    
    
    