#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:48:39 2019

@author: student
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:16:08 2019

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

classifier = Sequential()

classifier.add(Convolution2D(32,3,3 ,input_shape = (64,64,3), 
                             activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim = 128, activation = 'relu'))

classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',
                   metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

#train_datagen, test_datagen and generator functions taken from keras documentation
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '/home/student/Desktop/Python/dataset/pothole-detection-dataset/train_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_generator = test_datagen.flow_from_directory(
        '/home/student/Desktop/Python/dataset/pothole-detection-dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')


classifier.fit_generator(train_generator, samples_per_epoch = 8000,
                         nb_epoch = 10, validation_data = test_generator,
                         nb_val_samples = 2000)


