#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:53:38 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/Position_Salaries.csv')
x=df.iloc[:,1:2].values
y=df.iloc[:,2:3].values

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()

x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)

from sklearn.svm import SVR

regressor=SVR()
regressor.fit(x,y)

y_pred=regressor.predict(sc_x.fit_transform((np.array([6.5])).reshape(1,-1)))

y_pred=sc_y.inverse_transform(y_pred)

plt.scatter(x,y,color='k')
plt.plot(x,regressor.predict(x),color='r')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='k')
plt.plot(x_grid,regressor.predict(x_grid),color='r')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()




