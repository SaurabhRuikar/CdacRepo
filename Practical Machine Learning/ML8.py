#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:20:53 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Load packages
d=pd.read_csv('/home/student/Desktop/Python/Programs/Machine Learning/onewayanova.txt',sep='\t')
#generate a boxplot to see the data distribution by treatments
#between different treatments
d.boxplot(column=['A','B','C','D'],grid=False)

#Load packages
import scipy.stats as stats

#stats f_oneway functions takes the group as input and returns values
fvalue,pvalue=stats.f_oneway(d['A'],d['B'],d['C'],d['D'])
print(fvalue,pvalue)




import statsmodels.api as sm

d_melt=pd.melt(d.reset_index(),id_vars=['index'],value_vars=['A','B','C','D'])

d_melt.columns = ['Index','Performance','Value']
'''
model=ols('Value ~ C(Performance)',data=d_melt).fit()
anova_table=sm.stats.anova_lm(model,type=2)
print(anova_table)
'''

d_melt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

m_comp_res = pairwise_tukeyhsd(endog=d_melt['Value'],groups=d_melt['Performance'],alpha=0.05)
print(m_comp_res)