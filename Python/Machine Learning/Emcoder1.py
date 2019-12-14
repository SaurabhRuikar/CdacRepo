#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:48:43 2019

@author: student
"""


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import numpy as np
import pandas as pd
df = pd.read_csv('/home/student/DBDA_CHEATS/Python/dataset/weather_data.csv')
'''
x2 = df.iloc[:, 1:-1].values
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x2)
x2 = imputer.transform(x2)'''

df.fillna({'event':'Rain', 'temperature':12, 'windspeed':11}, inplace = True)
x = df.iloc[:, 1:].values
LabelEncoder_x = LabelEncoder()
x[:, -1] = LabelEncoder_x.fit_transform(x[:, -1])

onehot_x = OneHotEncoder(categorical_features = [-1])
x = onehot_x.fit_transform(x).toarray()
