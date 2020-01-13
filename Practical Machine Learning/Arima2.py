#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:23:07 2019

@author: student
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
from statsmodels.tsa.arima_model import ARIMA


plt.style.use('fivethirtyeight')

df=pd.read_csv("/home/student/Desktop/Python/dataset/movavg.csv",
               index_col='Date')
df.index=pd.to_datetime(df.index)

model=ARIMA(df.Price,order=(1,2,0))
model_fit=model.fit(disp=0)
print(model_fit.summary())