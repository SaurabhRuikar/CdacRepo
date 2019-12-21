#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:09:59 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/Housing.csv')
x=df.iloc[:,1:12].values
y=df.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
x[:,4]=labelencoder.fit_transform(x[:,4])
x[:,5]=labelencoder.fit_transform(x[:,5])
x[:,6]=labelencoder.fit_transform(x[:,6])
x[:,7]=labelencoder.fit_transform(x[:,7])
x[:,8]=labelencoder.fit_transform(x[:,8])
x[:,10]=labelencoder.fit_transform(x[:,10])
x=np.array(x,dtype=int)
print(x)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

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


import statsmodels.api as sm
from scipy import stats


#To get p-value
X_opt=x[:,[0,1,2,3,4,5,6,7,8,9,10]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary()) #To see all calculated values


