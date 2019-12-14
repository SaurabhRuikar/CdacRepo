#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:52:14 2019

@author: student
"""

#Systematic Sampling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_excel('/home/student/Desktop/Python/dataset/Linear_regression.xlsx')


lst1=[]
sr=len(dataset)
for x in range(1,sr):
    if x%5!=0:
        lst1.append(x)
        
lst2=[]
sr=len(dataset)
for x in range(1,sr):
    if x%5==0:
        lst2.append(x)
print(lst2)        

        
print(lst1)
df1=pd.read_excel('/home/student/Desktop/Python/dataset/Linear_regression.xlsx',skiprows=lst1)
X1_test=df1.iloc[:,-1].values.reshape(-1, 1)
y1_test=df1.iloc[:,1].values.reshape(-1, 1)




df2=pd.read_excel('/home/student/Desktop/Python/dataset/Linear_regression.xlsx',skiprows=lst2)
X1_train=df2.iloc[:,-1].values.reshape(-1,1)
y1_train=df2.iloc[:,1].values.reshape(-1,1)



from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X1_train,y1_train)


print("Coefficient:M",regressor.coef_)
print("Intercept: c",regressor.intercept_)


y1_pred=regressor.predict(X1_test)
v=np.array([9]).reshape(1,-1)
print(v.shape)

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
print("mean squared :",np.sqrt(mean_squared_error(y1_test,y1_pred)))
print("Mean absolute error :",mean_absolute_error(y1_test,y1_pred))
print("r2score:",r2_score(y1_test,y1_pred))


plt.scatter(X1_train,y1_train,color='red')
plt.plot(X1_train,regressor.predict(X1_train),color='black')
plt.title("For training data")
plt.xlabel("Yearly Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X1_test,y1_test,color='red')
plt.plot(X1_test,regressor.predict(X1_test),color='black')
plt.title("For testing data")
plt.xlabel("Yearly Experience")
plt.ylabel("Salary")
plt.show()

s=regressor.predict(v)
print(s)



