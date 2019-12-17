#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:58:33 2019

@author: student
"""

#Decision Tree Regressor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/student/Desktop/Python/dataset/Position_Salaries.csv')
x=df.iloc[:,1:2].values
y=df.iloc[:, 2].values

from sklearn.tree import DecisionTreeRegressor

regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)

y_pred=regressor.predict(np.array(6.5).reshape(1,-1))

x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='r')
plt.plot(x_grid,regressor.predict(x_grid),color='k')
plt.title('Truth or Bluff Decision Tree Regressor')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Random Forest Regressor

df = pd.read_csv('/home/student/Desktop/Python/dataset/Position_Salaries.csv')
x=df.iloc[:,1:2].values
y=df.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators=10,random_state=0)
regressor1.fit(x,y)

y_pred=regressor1.predict(np.array(6.5).reshape(1,-1))

x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='r')
plt.plot(x_grid,regressor1.predict(x_grid),color='k')
plt.title('Truth or Bluff Decision Tree Regressor')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()








