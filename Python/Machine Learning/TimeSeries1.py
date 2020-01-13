#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:08:19 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates = ['date'], index_col = 'date')

def plot_df(df, x, y, title = '', xlabel = 'Date', ylabel = 'Value', dpi = 100):
    plt.figure(figsize = (5, 4), dpi = dpi)
    plt.plot(x, y, color = 'tab:red')
    plt.gca().set(title = title, xlabel = xlabel, ylabel = ylabel)
    plt.show()
    
plot_df(df, x = df.index, y = df.value, title = 'Monthly Anti Dibetic Drug')