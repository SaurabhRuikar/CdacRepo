#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:51:26 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.layers import Input, Dense
from keras.models import Model

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

from keras.datasets import fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
y_train = onehotencoder.fit_transform(y_train).toarray()
y_test = onehotencoder.transform(y_test).toarray()

X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

classifier = Sequential()

classifier.add(Convolution2D(32,3,3 ,input_shape = (28, 28, 1), 
                             activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))


classifier.add(Flatten())


classifier.add(Dense(output_dim = 128, activation = 'relu'))

classifier.add(Dense(output_dim = 10, activation = 'softmax'))

classifier.compile(optimizer='adam',loss='categorical_crossentropy',
                   metrics=['accuracy'])

classifier.fit(X_train, y_train, epochs = 100)





