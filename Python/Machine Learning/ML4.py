#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:16:56 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
d=np.random.normal(size=1000)
d


sns.distplot(d,bins=None,
             hist=True,kde=True,ax=None,color='r')
'''

from scipy.stats import ttest_1samp
ages=np.random.normal(20,40,1000)

ages_mean=np.mean(ages)
print("Mean :",ages_mean)

#h0=average age is 30
ttest,pval=ttest_1samp(ages,30)
print("p values: ",pval)
if pval<0.05:
    print("Null Hypothesis Rejected")
else:
    print("Null Hypothesis Accepted")

    