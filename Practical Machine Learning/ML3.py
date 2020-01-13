#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:42:57 2019

@author: student
"""

#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Importing the dataset(At 4 th line in excel file Header is present so Header=4)
df=pd.read_excel(r'/home/student/Desktop/Python/dataset/Multple Regression Analyisis_1.xlsx',"Sheet1",header=3)


X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

#Splitting data into Training and Testing set
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

#To calculate r2 scores and errors
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
print('mean squared error :',np.sqrt(mean_squared_error(y_test,y_pred)))
print('mean absolute error :',(mean_absolute_error(y_test,y_pred)))
print('r^2 score',r2_score(y_test,y_pred))


#To get t-test and P Value
import statsmodels.api as sm
from scipy import stats

#adding extra column at the begining
#X=np.append(arr=np.ones((322,1)),values=X,axis=1)




#To get p-value
X_opt=X[:,[0,1,2,3,4]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())

