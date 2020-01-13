#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:45:20 2019

@author: student
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Importing the dataset
dataset=pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',na_values=["n.a.","not available"])
X=dataset.iloc[:, :].values
print(X)
print(type(X))



#Taking care of missing data
from sklearn.preprocessing import Imputer
#create a object of Imputer class
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:, 1:4])
X[:, 1:4]=imputer.transform(X[:, 1:4])
print(X)


dataset2=pd.read_csv('/home/student/Desktop/Python/dataset/comb1.csv')
X2=dataset2.iloc[:, -1].values.reshape(-1,1)
print(X2)

from sklearn.preprocessing import Imputer
impmedian = Imputer(missing_values='NaN', strategy='median',axis=0)
impmedian=impmedian.fit(X2)
X2=impmedian.transform(X2)
X2=pd.DataFrame(X2)


#SimpleImputer
dataset3=pd.read_csv('/home/student/Desktop/Python/dataset/comb1.csv')
X3=dataset3.iloc[:, -1].values.reshape(-1,1)
print(X3)

from sklearn.impute import SimpleImputer
impmedian= SimpleImputer(missing_values=np.nan, strategy='median')
impmedian.fit(X3)
X3=pd.DataFrame(impmedian.transform(X3))
#X3=pd.DataFrame(X3)

#Encoding categorical data
#Encoding the independent variable

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,1]=labelencoder_X.fit_transform(X[:,1]) #X should be ndarray so don't convert in dataframe


onehotencoder=OneHotEncoder(categorical_features=[1])
X=onehotencoder.fit_transform(X).toarray()



print(X)


#To use one object for multiple columns

onehotencoder=OneHotEncoder()
categorical_features=[4]
X_oneHotEncoded=onehotencoder.fit_transform(X[:,categorical_features]).toarray()
X_final=np.hstack((X[:,:4],X_oneHotEncoded))
print(X_final)





