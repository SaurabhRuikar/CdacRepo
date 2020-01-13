#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:09:50 2019

@author: student
"""
#INDEPENDENT t-test
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

ds1=np.random.normal(2.3,0.9,1000)
ds2=np.random.normal(1.8,0.7,1000)
print(ds1)
print("ds2 data :-\n")
print(ds2)



ds1_mean=np.mean(ds1)
ds2_mean=np.mean(ds2)
print("ds1 mean value :",ds1_mean)
print("ds2 mean value :",ds2_mean)

ds1_std=np.std(ds1)
ds2_std=np.std(ds2)
print("ds1 mean value :",ds1_std)
print("ds2 mean value :",ds2_std)



ttest,pval=ttest_ind(ds1,ds2)
print("p values: ",pval)
if pval<0.05:
    print("Null Hypothesis Rejected")
else:
    print("Null Hypothesis Accepted")
    
    
#Related t-test

from scipy import stats
ds1=np.random.normal(80,120,1000)
ds2=np.random.normal(80,120,1000)

ttest,pval=stats.ttest_rel(ds1,ds2)
print("p values: ",pval)
if pval<0.05:
    print("Null Hypothesis Rejected")
else:
    print("Null Hypothesis Accepted")
    