#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:10:06 2019

@author: student
"""
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,id=0,name="",balance=0):
        self.id=id
        self.name=name
        self.balance=balance
        super().__init__()
        
        
    def __str__(self):
        return "Id : "+str(self.id)+"\nName : "+self.name+"\nBalance : "+str(self.balance)
    
    @abstractmethod
    def withdraw(self,amt=""):
        pass
    def depos(self,amt=0):
        self.balance=self.balance+amt
    
    
    
    
    
class SavingAcc(Account):
    interestRate=0.8
    def __init__(self,id=0,name="",balance=0,chequebookno=""):
        Account.__init__(self,id,name,balance)
        self.chequebookno=chequebookno
        
    def __str__(self):
        return Account.__str__(self)+"\nChequeBook No : "+self.chequebookno

    def withdraw(self,amt=0):
        ans=self.balance-amt
        if ans<25000:
            print("Insufficient ")
        else:
            self.balance=ans
            
         
        
        
    

    
    def getId(self):
        return self.id
    
    def getBal(self):
        return self.balance


class CurrentAcc(Account):
    noot=7
    def __init__(self,id=0,name="",balance=0,creditcardnum=""):
        Account.__init__(self,id,name,balance)
        #self.numtransactions=numtransactions
        self.creditcardnum=creditcardnum
        
    def __str__(self):
        return Account.__str__(self)+ "\nCredit Card number : "+self.creditcardnum
    

    def withdraw(self,amt=0):
        ans=self.balance-amt
        if ans<50000:
            print("Insufficient ")
        else:
            self.balance=ans
     
  
    

    def getId(self):
        return self.id    
    
    def getBal(self):
        return self.balance

'''
ob=CurrentAcc(1,"saurabh",100,6,"287279")
print(ob)
'''