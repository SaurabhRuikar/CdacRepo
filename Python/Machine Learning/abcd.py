#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:58:54 2019

@author: student
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_data=np.linspace(0.0,10.0,1000000)
noise=np.random.randn(len(x_data))
print(x_data)
print(noise)

y_true=(0.5*x_data)+5+noise

x_df=pd.DataFrame(data=x_data,columns=['X_Data'])
y_df=pd.DataFrame(data=y_true,columns=['Y'])

print(x_df.head())
print(y_df.head())


my_data=pd.concat([x_df,y_df],axis=1)

print(my_data.head())

my_data.sample(n=250).plot(kind='scatter',x='X_Data',y='Y')


feat_cols=[tf.feature_column.numeric_column('x',shape=[1])]

estimator=tf.estimator.LinearRegressor(feature_columns=feat_cols)


from sklearn.model_selection import train_test_split

x_train,x_eval,y_train,y_eval=train_test_split(x_data,y_true,test_size=0.3,random_state=0)

input_func=tf.estimator.inputs.numpy_input_fn({'x': x_train}, y_train,batch_size=4, num_epochs = None, shuffle=True)

train_input_func=tf.estimator.inputs.numpy_input_fn({'x': x_train}, y_train,batch_size=4, num_epochs = 1000, shuffle=False)

eval_input_func=tf.estimator.inputs.numpy_input_fn({'x': x_train}, y_train,batch_size=4, num_epochs = 1000, shuffle=False)

estimator.train(input_fn=input_func,steps=1000)

train_metrics = estimator.evaluate(input_fn= train_input_func, steps=1000)

eval_metrics =  estimator.evaluate(input_fn= eval_input_func, steps=1000)
eval_metrics

input_fu_predict= tf.estimator.inputs.numpy_input_fn({'x':np.linspace(0,10,10)}, shuffle=False)

lst = estimator.predict(input_fn = input_fu_predict)
print(lst) 



