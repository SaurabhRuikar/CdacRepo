#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:17:05 2019

@author: student
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('/home/student/Desktop/Python/dataset/Churn_Modelling.csv')

numeric_col = ['CreditScore', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']

df[numeric_col] = df[numeric_col].apply(lambda x : (x - x.min())/(x.max() - x.min()))

CreditScore = tf.feature_column.numeric_column('CreditScore')
Tenure = tf.feature_column.numeric_column('Tenure')
Balance = tf.feature_column.numeric_column('Balance')
NumOfProducts = tf.feature_column.numeric_column('NumOfProducts')
HasCrCard = tf.feature_column.numeric_column('HasCrCard')
IsActiveMember = tf.feature_column.numeric_column('IsActiveMember')
EstimatedSalary = tf.feature_column.numeric_column('EstimatedSalary')
Age = tf.feature_column.numeric_column('Age')

#Does Label Encoding and One hot Encoding Internally
Gender = tf.feature_column.categorical_column_with_vocabulary_list('Gender', ['Male','Female'])
Georgaphy = tf.feature_column.categorical_column_with_vocabulary_list('Geography', ['France', 'Spain', 'Germany'])

minval = df['Age'].min()
maxval = df['Age'].max()

Age = tf.feature_column.bucketized_column(Age, boundaries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

feature_col = [CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary, Gender, Georgaphy]

X_data = df.drop('Exited', axis = 1)
labels = df['Exited']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data, labels, test_size = 0.3, random_state = 0)

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


               
