#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:19:18 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose 

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                   parse_dates = ['date'], index_col = 'date')

result_mul=seasonal_decompose(df['value'],model='multiplicative',extrapolate_trend='freq')

result_add=seasonal_decompose(df['value'],model='additive',extrapolate_trend='freq')

plt.rcParams.update({'figure.figsize':(10,10)})
result_mul.plot().suptitle('Multiplicative Decompose',fontsize=22)
result_add.plot().suptitle('Additive Decompose',fontsize=22)
plt.show()



df_reconstructed_add=pd.concat([result_add.seasonal,result_add.trend,result_add.resid,result_add.observed],axis=1)
df_reconstructed_add.columns=['seas','trend','resid','actual values']
df_reconstructed_add.head()

df_reconstructed_mul=pd.concat([result_mul.seasonal,result_mul.trend,result_mul.resid,result_mul.observed],axis=1)
df_reconstructed_mul.columns=['seas','trend','resid','actual values']
df_reconstructed_mul.head()