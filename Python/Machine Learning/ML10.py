#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:47:12 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib
#matplotlib.rcParams.update({'font:size':12})
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

boston=load_boston()
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df['Price']=boston.target

newX=boston_df.drop('Price',axis=1)
print(newX[0:3])

newY=boston_df['Price']

X_train,X_test,y_train,y_test=train_test_split(newX,newY,test_size=0.2,random_state=0)
print(len(X_test),len(y_test))
lr=LinearRegression()
lr.fit(X_train,y_train)
print()

print('Coefficients : ',lr.coef_)
print('Intercept : ',lr.intercept_)
print('Train score : ',lr.score(X_train,y_train))
print('Test score : ',lr.score(X_test,y_test))
print()


rr=Ridge(alpha=0.01)
rr.fit(X_train,y_train)
print('Ridge with Alpha 0.01')
print('Coefficients : ',rr.coef_)
print('Intercept : ',rr.intercept_)
print('Train score : ',rr.score(X_train,y_train))
print('Test score : ',rr.score(X_test,y_test))
print()


rr50=Ridge(alpha=50)
rr50.fit(X_train,y_train)
print('Ridge with Alpha 50')
print('Coefficients : ',rr50.coef_)
print('Intercept : ',rr50.intercept_)
print('Train score : ',rr50.score(X_train,y_train))
print('Test score : ',rr50.score(X_test,y_test))
print()


rr75=Ridge(alpha=75)
rr75.fit(X_train,y_train)
print('Ridge with Alpha 75')
print('Coefficients : ',rr75.coef_)
print('Intercept : ',rr75.intercept_)
print('Train score : ',rr75.score(X_train,y_train))
print('Test score : ',rr75.score(X_test,y_test))
print()


print()
rr100=Ridge(alpha=100)
rr100.fit(X_train,y_train)
print('Ridge with Alpha 100')
print('Coefficients : ',rr100.coef_)
print('Intercept : ',rr100.intercept_)
print('Train score : ',rr100.score(X_train,y_train))
print('Test score : ',rr100.score(X_test,y_test))
print()
print()







ll=Lasso(alpha=0.01)
ll.fit(X_train,y_train)
print('Lasso with Alpha 0.01')
print('Coefficients : ',ll.coef_)
print('Intercept : ',ll.intercept_)
print('Train score : ',ll.score(X_train,y_train))
print('Test score : ',ll.score(X_test,y_test))
print()


ll50=Lasso(alpha=50)
ll50.fit(X_train,y_train)
print('Lasso with Alpha 50')
print('Coefficients : ',rr50.coef_)
print('Intercept : ',rr50.intercept_)
print('Train score : ',rr50.score(X_train,y_train))
print('Test score : ',rr50.score(X_test,y_test))
print()


print()
ll100=Lasso(alpha=100)
ll100.fit(X_train,y_train)
print('Lasso with Alpha 100')
print('Coefficients : ',rr100.coef_)
print('Intercept : ',rr100.intercept_)
print('Train score : ',rr100.score(X_train,y_train))
print('Test score : ',rr100.score(X_test,y_test))


