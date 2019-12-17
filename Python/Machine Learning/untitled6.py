#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:22:30 2019

@author: student
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/age.csv')

#MULTIPLE LINEAR REGRESSION

df=df.iloc[:,0:9]

X=df.iloc[:,1:8].values
y=df.iloc[:,8:9].values

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
y1_test=StandardScaler()

x=sc_x.fit_transform(X)
y=sc_y.fit_transform(y)
y_test2=y1_test.fit_transform(y_test)


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