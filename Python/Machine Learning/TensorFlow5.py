#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:27:52 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y = True)

feat_cols = [tf.feature_column.numeric_column('x', shape=[4])]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size = 0.3, 
                                                    random_state = 0)


input_func = tf.estimator.inputs.numpy_input_fn({"x" : X_train}, 
                                                 y_train, 
                                                 batch_size = 10, 
                                                 num_epochs = 1000, 
                                                 shuffle = True)

model = tf.estimator.LinearClassifier(feature_columns = feat_cols,
                                            n_classes = 3)

model.train(input_fn = input_func, steps = 1000)

eval_input_func = tf.estimator.inputs.numpy_input_fn({"x" : X_test},
                                                      y_test,
                                                      batch_size = 10,
                                                      num_epochs = 1,
                                                      shuffle = False)

results = model.evaluate(eval_input_func)

pred_input_func = tf.estimator.inputs.numpy_input_fn({'x' : X_test},
                                                      batch_size = 10,
                                                      shuffle = False) 

prediction = model.predict(input_fn = pred_input_func)

my_pred = list(prediction)

for i in my_pred:
    for k, j in i.items():
        if k == 'probabilities':
            print(j)


