s#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:13:22 2019

@author: student
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('fivethirtyeight')

data=pd.read_csv("/home/student/Desktop/Python/dataset/movavg.csv",index_col='Date')
data.index=pd.to_datetime(data.index)
data=data.drop(columns='Unnamed: 0')
data
weights=np.arange(1,11)

weights

#data.columns

sma10=data['Price'].rolling(10).mean()
sma10
wma10=data['Price'].rolling(10).apply(lambda prices:np.dot(prices,weights)/weights.sum(),0)
wma10.head(10)
#
#type(wma10)
#type(sma10)

plt.figsize=(12,6)
plt.plot(data['Price'],label="Price")
plt.plot(wma10,label="10-day WMA")
plt.plot(sma10,label="10-day SMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.plot(sma10)
plt.plot(wma10)


ema10=data['Price'].ewm(span=10).mean()
ema10.head(10)
#ema10.plot()

plt.figsize=(12,6)
plt.plot(ema10,color='y',label="10-day EMA")
plt.xlabel("Date")
plt.legend()
