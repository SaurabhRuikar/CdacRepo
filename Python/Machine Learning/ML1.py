#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:20:31 2019

@author: student
"""

import numpy as np
import pandas as pd


df=pd.read_csv('/home/student/Desktop/Python/dataset/50_Startups.csv',na_values=0)
df
X=df.iloc[:,0:4].values
y=df.iloc[:,-1].values
#z=df.iloc[:,:-1] To skip last column





from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:, 0:3])
X[:, 0:3]=imputer.transform(X[:, 0:3])
print(X)



from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3]) #X should be ndarray so don't convert in dataframe


onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()

print(X)





