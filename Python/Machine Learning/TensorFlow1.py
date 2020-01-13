#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:34:25 2019

@author: student
"""

#Need to have tensorflow version 1.1x
#Version 2.x does not have Session Command

#If version 2.x 
#import tensorflow.compat.v1 as tf
#tf.disable_v2_behaviour()

import tensorflow as tf

#Version
print(tf.__version__)

hello = tf.constant('Hello')

world = tf.constant('World!')

type(hello)

print(hello)         #not actual output but the data of the variable

#Creating and Running the session
with tf.Session() as sess:
    result = sess.run(hello+world)
    
print(result)

##########################################################################

#Simple Addition

a =  tf.constant(10)

b =  tf.constant(20)

c = a+b

#Generates variable and stores output but does not display it
print(c)

with tf.Session() as sess:
    result = sess.run(c)

print(result)

#########################################################################

const = tf.constant(10)

mat_1 = tf.fill((5,5),10)

zeroes = tf.zeros((5,5))

ones = tf.ones((5,5))

#Scope of Session only limited to the With Loop
with tf.Session() as sess:
    result = sess.run(const)
    result1 = sess.run(mat_1)
    result2 = sess.run(zeroes)
    result3 = sess.run(ones)

print(result)
print(result1)
print(result2)
print(result3)


#Alternative Approach for Session

const = tf.constant(10)

mat_1 = tf.fill((5,5),10)

zeroes = tf.zeros((5,5))

ones = tf.ones((5,5))

randn = tf.random_normal((4,4), mean = 0, stddev = 1.0)

randu = tf.random_uniform((4,4), minval = 0, maxval = 1)

myops = [const, mat_1, zeroes, ones, randn, randu]

#Session Stays active until we close it explicitly.
#No need to use With Loop in this case

sess = tf.InteractiveSession()

for op in myops:
    print(op.eval())
    print('\n')

#Closing Session
sess.close()

#####################################################################
    

sess = tf.InteractiveSession()

a = tf.constant([[1,2],[3,4]])

a.get_shape()                  #Size - 2x2

b = tf.constant([[10],[100]])

b.get_shape()                  #Size - 2x1

#Matrix Multiplication
result = tf.matmul(a,b)

sess.run(result)

###########################################################################


#TensorBoard Graphs

a =  tf.constant(10)

b =  tf.constant(20)

c = a+b

with tf.Session() as sess:
    result = sess.run(c)

print(result)

print(c)

#Creates a graph object
print(tf.get_default_graph())

#To create graphs
g = tf.Graph()
print(g)

#To change the default graph object
g_1 = tf.get_default_graph()
print(g_1)

sess.close()

##########################################################################

sess = tf.InteractiveSession()

my_tensor = tf.random_uniform((5,5),0,2)

my_tensor


                                #Variables

var1 = tf.Variable(initial_value = my_tensor)

print(var1)

init = tf.global_variables_initializer()

sess.run(init)

sess.run(var1)


                               #PlaceHolders

#Any no of rows, only 4 columns
pH1 = tf.placeholder(tf.float32, shape  =(None, 4))

#When you do not know num of rows and columns
pH2 = tf.placeholder(tf.float32)


##########################################################################

#ANN Demonstration Using TensorFlow

import numpy as np

n_f = 10

n_d_n = 3

x = tf.placeholder(tf.float32,(None, n_f))

b = tf.Variable(tf.zeros([n_d_n]))

w = tf.Variable(tf.random_normal([n_f, n_d_n]))

xw = tf.matmul(x, w)

z = tf.add(xw , b)

a = tf.sigmoid(z)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    layer_out = sess.run(a, feed_dict = { x: np.random.random([1, n_f])})

print(layer_out)

##########################################################################

x_data = np.linspace(0, 10, 10) + np.random.uniform(-1.5, 1.5, 10)

x_data

y_label = np.linspace(0, 10, 10) + np.random.uniform(-1.5, 1.5, 10)

import matplotlib.pyplot as plt

plt.plot(x_data, y_label, '*')


#Without Adding Noise we will get a straight line so we have used np.random above

#x_data = np.linspace(0, 10, 10)
#
#x_data
#
#y_label = np.linspace(0, 10, 10) 
#
#import matplotlib.pyplot as plt
#
#plt.plot(x_data, y_label, '*')

np.random.rand(2)

m = tf.Variable(0.79)

b = tf.Variable(0.68)

error = 0

for x,y in zip(x_data, y_label):
    y_hat = m * x + b
    
    error += (y - y_hat)**2
    
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
train = optimizer.minimize(error)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    
    sess.run(init)
    
    epochs = 100
        
    for i in range(epochs):
        sess.run(train)
        
    final_slope, final_intercept = sess.run([m, b])


print(final_slope)

print(final_intercept)    
        
x_test = np.linspace(-1, 11, 10)

y_pred_plot = final_slope * x_test + final_intercept

plt.plot(x_test, y_pred_plot, 'g')

plt.plot(x_data, y_label, '*')   
