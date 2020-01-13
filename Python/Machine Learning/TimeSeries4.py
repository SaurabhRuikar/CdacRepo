#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:54:00 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                   parse_dates = ['date'], index_col = 'date')

result = adfuller(df.value.values, autolag = 'AIC')
print(f'ADF Statistics : {result[0]}')
print(f'P Value : {result[1]}')

for key, value in result[4].items():
    print('Critical value : ', end = '')
    print(f'{key}, {value}')

result = kpss(df.value.values, regression = 'c')
print(f'\nKPSS Statistics : {result[0]}')
print('P Value : %f' %result[1])

for key, value in result[3].items():
    print('Critical value : ', end = '')
    print(f'{key}, {value}')
        