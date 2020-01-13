#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:43:56 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('/home/student/Desktop/Python/dataset/diabetes.csv')

print(df.head())

numeric_col = ['Number_pregnant', 'Glucose_concentration', 'Blood_pressure', 'Triceps',
       'Insulin', 'BMI', 'Pedigree']

df[numeric_col] = df[numeric_col].apply(lambda x : (x - x.min())/(x.max() - x.min()))

Number_pregnant = tf.feature_column.numeric_column('Number_pregnant')
Glucose_concentration = tf.feature_column.numeric_column('Glucose_concentration')
Blood_pressure = tf.feature_column.numeric_column('Blood_pressure')
Triceps = tf.feature_column.numeric_column('Triceps')
Insulin = tf.feature_column.numeric_column('Insulin')
BMI = tf.feature_column.numeric_column('BMI')
Pedigree = tf.feature_column.numeric_column('Pedigree')
Age = tf.feature_column.numeric_column('Age')

Groups = tf.feature_column.categorical_column_with_vocabulary_list('Group', ['A','B','C','D'])
minval = df['Age'].min()
maxval = df['Age'].max()
Age = tf.feature_column.bucketized_column(Age, boundaries = [20, 30, 40, 50, 60, 70, 80])

feature_col = [Number_pregnant, Glucose_concentration, Blood_pressure, Triceps,
       Insulin, BMI, Pedigree, Age, Groups]

X_data = df.drop('Class', axis = 1)
labels = df['Class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data,
                                                    labels, 
                                                    test_size = 0.3, 
                                                    random_state = 0)

input_func = tf.estimator.inputs.pandas_input_fn(x = X_train, 
                                                 y = y_train, 
                                                 batch_size = 10, 
                                                 num_epochs = 1000, 
                                                 shuffle = True)
model = tf.estimator.LinearClassifier(feature_columns = feature_col,
                                            n_classes = 2)

model.train(input_fn = input_func, steps = 1000)

eval_input_func = tf.estimator.inputs.pandas_input_fn(x = X_test,
                                                      y = y_test,
                                                      batch_size = 10,
                                                      num_epochs = 1,
                                                      shuffle = False)

results = model.evaluate(eval_input_func)

pred_input_func = tf.estimator.inputs.pandas_input_fn(x = X_test,
                                                      batch_size = 10,
                                                      shuffle = False) 

prediction = model.predict(input_fn = pred_input_func)

my_pred = list(prediction)

#print(my_pred)

for i in my_pred:
    for k, j in i.items():
        if k == 'probabilities':
            print(j)

