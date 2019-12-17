#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:53:21 2019

@author: student
"""

#Systematic Sampling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a1=[6,4,5,10]
a2=[8,5,3,3]
a3=[5,4,8,4]
a4=[4,11,7,13]
a5=[5,8,7,6]
a6=[7,3,5,9]
a7=[7,3,5,9]

dice = np.array([a1,a2,a3,a4,a5,a6,a7])
from scipy import stats

chi2_stat,p_val,dof,ex=stats.chi2_contingency(dice)
print('Chi2 Square' )
print(chi2_stat)
print()
print('Degree of Freedom')
print(dof)
print()
print('P value ')
print(p_val)
print()
print('Contingency Table ')
print(ex)