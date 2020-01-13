#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:59:56 2019

@author: student
"""

#Systematic Sampling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Systematic Sampling
dataset=pd.read_excel('/home/student/Desktop/Python/dataset/Linear_regression.xlsx')
lst2=[]
sr=len(dataset)
for x in range(1,sr):
    if x%5==0:
        lst2.append(x)
print(lst2)      

df2=pd.read_excel('/home/student/Desktop/Python/dataset/Linear_regression.xlsx',skiprows=lst2)
X1_train=df2.iloc[:,-1].values.reshape(-1,1)


#Random Sampling
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


#Splitting dataset into Training and Testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)



X_train_mean=np.mean(X_train)
X1_train_mean=np.mean(X1_train)
print("X_train mean value :",X_train_mean)
print("X1_train mean value :",X1_train_mean)

X_train_std=np.std(X_train)
X1_train_std=np.std(X1_train)
print("X_train std value:",X_train_std)
print("X1_train std  value :",X1_train_std)



ttest,pval=ttest_ind(X_train,X1_train)
print("p values: ",pval)
if pval<0.05:
    print("Null Hypothesis Rejected")
else:
    print("Null Hypothesis Accepted")