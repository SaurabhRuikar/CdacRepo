# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:00:28 2018

@author: ss
"""

import pandas as pd

cars = pd.read_csv("F:/Python Material/ML with Python/Datasets/Cars93.csv")

cars.head(n=10)

dum_cars = pd.get_dummies(cars, drop_first=True)

dum_cars.head(n=10)

carsMissing = pd.read_csv("F:/Python Material/ML with Python/Datasets/Cars93Missing.csv")
carsMissing.shape

carsDropNA = carsMissing.dropna()
carsDropNA.shape

# Dummying the data
dum_cars_miss = pd.get_dummies(carsMissing, drop_first=True)

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(dum_cars_miss)
carsImputed = imp.transform(dum_cars_miss)


dum_cars_miss.shape
carsImputed.shape

import numpy as np
milk = pd.read_csv("F:/Python Material/Python Course/Datasets/milk.csv",index_col=0)
milk.head()
np.mean(milk), np.std(milk)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)
np.mean(milkscaled[:,0]), np.std(milkscaled[:,0])
np.mean(milkscaled[:,1]), np.std(milkscaled[:,1])
np.mean(milkscaled[:,2]), np.std(milkscaled[:,2])
np.mean(milkscaled[:,3]), np.std(milkscaled[:,3])
np.mean(milkscaled[:,4]), np.std(milkscaled[:,4])


from sklearn.preprocessing import Normalizer
normalize = Normalizer()
normalize.fit(milk)
normMilk = normalize.transform(milk)
normMilk[1:5,]