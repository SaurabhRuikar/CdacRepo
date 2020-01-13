#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:33:58 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv')


fig, axes = plt.subplots(1, 2, figsize = (16, 3), dpi = 100)
plot_acf(df.value.tolist(), lags = 50, ax = axes[0])
plot_pacf(df.value.tolist(), lags = 50, ax = axes[1])