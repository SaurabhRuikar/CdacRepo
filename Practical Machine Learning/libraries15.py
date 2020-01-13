#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:35:04 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Importing the dataset
dataset=pd.read_csv('/home/student/Desktop/Python/dataset/Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


#Splitting dataset into Training and Testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)




from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)


#to print coefficient and intercept
print("Coefficient:M",regressor.coef_)
print("Intercept: c",regressor.intercept_)

#Preceding the Test set results

y_pred=regressor.predict(X_test)
v=np.array([6.8]).reshape(1,-1)
print(v.shape)


s=regressor.predict(v)
print(s)




from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
print("mean squared :",np.sqrt(mean_squared_error(y_test,y_pred)))
print("Mean absolute error :",mean_absolute_error(y_test,y_pred))
print("r2score:",r2_score(y_test,y_pred))


plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='black')
plt.title("For training data")
plt.xlabel("Yearly Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test,y_test,color='red')
plt.plot(X_test,regressor.predict(X_test),color='black')
plt.title("For testing data")
plt.xlabel("Yearly Experience")
plt.ylabel("Salary")
plt.show()



'''
datasets[..klds] = datasets[..klds].apply(lambda x : x.lstrip('$'))
'''


