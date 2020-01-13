#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:06:52 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/sunspotarea.csv',
                   parse_dates = ['date'], index_col = 'date')

df2 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/guinearice.csv',
                   parse_dates = ['date'], index_col = 'date')

df3 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv',
                   parse_dates = ['date'], index_col = 'date')

def plot_df(df, x, y, title = '', xlabel = 'Date', ylabel = 'Value', dpi = 100):
    plt.figure(figsize = (5, 4), dpi = dpi)
    plt.plot(x, y, color = 'tab:red')
    plt.gca().set(title = title, xlabel = xlabel, ylabel = ylabel)
    plt.show()
    
plot_df(df1, x = df1.index, y = df1.value, title = 'SunspotArea')
plot_df(df2, x = df2.index, y = df2.value, title = 'Guinearice')
plot_df(df3, x = df3.index, y = df3.value, title = 'AirPassengers')