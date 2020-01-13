#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:45:20 2019

@author: student
"""

'''
1)
Using age file desgn all possible linear or non linear regression models.
Check whether all parameters are important to consider for calculating weight.
Decide which Model gives you good results.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/age.csv')

#MULTIPLE LINEAR REGRESSION

df=df.iloc[:,0:9]

X=df.iloc[:,1:8].values
y=df.iloc[:,8:9].values


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



#OLS


import statsmodels.api as sm
from scipy import stats

X_opt=X[:,[0,1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())

#Polynomial Regression cannot be achieved as x and y are not of the same size

#SVR

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()

x=sc_x.fit_transform(X)
y=sc_y.fit_transform(y)

from sklearn.svm import SVR

regressor=SVR()
regressor.fit(x,y)

y_pred=regressor.predict(sc_x.fit_transform((np.array([6.5,7.1,2.0,3.5,5.6,6.2,7.0])).reshape(1,-1)))

y_pred=sc_y.inverse_transform(y_pred)

print(y_pred)


import statsmodels.api as sm
from scipy import stats

X_opt=x[:,[0,1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())

'''
X_opt=x[:,[1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())
'''
#No need to delete above record as no change in adjusted r^2 Score


#DECISION TREE REGRESSOR

from sklearn.tree import DecisionTreeRegressor

regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)
    

#y_pred=regressor.predict(sc_x.fit_transform((np.array([6.5,7.1,2.0,3.5,5.6,6.2,7.0])).reshape(1,-1)))
y_pred=regressor.predict(np.array([6.5,7.1,2.0,3.5,5.6,6.2,7.0]).reshape(1,-1))
print(y_pred)

X_opt=X[:,[0,1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())

#Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators=10,random_state=0)
regressor1.fit(X,y)

y_pred=regressor1.predict(np.array([6.5,7.1,2.0,3.5,5.6,6.2,7.0]).reshape(1,-1))
print(y_pred)

X_opt=X[:,[0,1,2,3,4,5,6]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt)
s=regressor_OLS.fit()
print(s.summary())


