#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:25:51 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import autocorrelation_plot

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv')

plt.rcParams.update({'figure.figsize':(9, 5),'figure.dpi':120})
autocorrelation_plot(df.value.tolist())
