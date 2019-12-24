#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:15:44 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/Churn_Modelling.csv')

X=df.iloc[:, 3:13].values
y=df.iloc[:, 13].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X_1=LabelEncoder()
X[:, 1]=labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2=LabelEncoder()
X[:, 2]=labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder=OneHotEncoder(categorical_features = [1])
X=onehotencoder.fit_transform(X).toarray()
X=X[:,1:]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

import keras 

from keras.models import Sequential

from keras.layers import Dense

classifier=Sequential()

#Input Layer
classifier.add(Dense(output_dim=6,init='uniform',activation='relu',input_dim=11))

#Hidden Layer
classifier.add(Dense(output_dim=12,init='uniform',activation='relu'))

classifier.add(Dense(output_dim=6,init='uniform',activation='relu'))

#Output Layer
classifier.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))

#Compiling
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Fitting the model
classifier.fit(X_train,y_train,batch_size=10,nb_epoch=100)

#Prediction
y_pred=classifier.predict(X_test)

#Will Give answer in True or False
y_pred=(y_pred > 0.5)

#Verifying the accuracy using confusin matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)




