#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:01:22 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv')

model=ARIMA(df.value,order=(1,1,2))
model_fit=model.fit(disp=0)
print(model_fit.summary())

model=ARIMA(df.value,order=(1,1,1))
model_fit=model.fit(disp=0)
print(model_fit.summary())

model=ARIMA(df.value,order=(0,0,0))
model_fit=model.fit(disp=0)
print(model_fit.summary())