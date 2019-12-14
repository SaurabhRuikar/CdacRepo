#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:29:27 2019

@author: student
"""

import numpy as np
import pandas as pd


df=pd.read_csv('/home/student/Desktop/Python/dataset/50_Startups.csv')
df
X=df.iloc[:,0:4].values
y=df.iloc[:,-1].values
print(X)
#z=df.iloc[:,:-1] To skip last column





from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values=0,strategy='mean',axis=0)
imputer=imputer.fit(X[:, 0:3])
X[:, 0:3]=imputer.transform(X[:, 0:3])
print(X)

