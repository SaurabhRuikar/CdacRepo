#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:29:26 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/Position_Salaries.csv')

X=df.iloc[:,1:2].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


#Fitting Multiple Linear Reg to Training Set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Printing Coefficients
print('Coefficients : ',regressor.coef_)
print('Intercept : ',regressor.intercept_)


#Predicting test set Results
y_pred=regressor.predict(X_test)



plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='black')
plt.title("Train")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test,y_test,color='red')
plt.plot(X_test,regressor.predict(X_test),color='black')
plt.title("For testing data")
plt.xlabel("Level")
plt.ylabel  ("Salary")
plt.show()


#Fitting it with Polynomial Regression 
from sklearn.preprocessing import PolynomialFeatures

for i in range(3,7):
    print('Degree = ',i)
    poly_reg=PolynomialFeatures(degree=i)
    X_poly= poly_reg.fit_transform(X)
    poly_reg.fit(X_poly,y)
    lin_reg2=LinearRegression()
    lin_reg2.fit(X_poly,y)
    
    print('Coefficients : ',lin_reg2.coef_)
    print('Intercept : ',lin_reg2.intercept_)
    print()

    plt.scatter(X,y,color='r')
    plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color='b')
    plt.title("Train")
    plt.xlabel("Level") 
    plt.ylabel("Salary")
    plt.show()
    
    


















