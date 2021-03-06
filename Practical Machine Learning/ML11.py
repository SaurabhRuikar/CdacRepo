#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:07:10 2019

@author: student
"""

import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('whitegrid')

avg=1
std_dev=0.1
num_reps=500
num_simulations=1000
pct_to_target=np.random.normal(avg,std_dev,num_reps).round(2)


sales_target_values=[75_000,100_000,200_000,100_000,400_000,500_000]
sales_target_prob=[.3,.3,.2,.1,.05,.05]
sales_target=np.random.choice(sales_target_values,num_reps,p=sales_target_prob)


sales_target[0:10]
df=pd.DataFrame(index=range(num_reps),data={'Pct_To_Target':pct_to_target,"Sales_Target":sales_target})
df.head()

df['Sales']= df['Pct_To_Target'] * df['Sales_Target']

def calc_commision_rate(x):
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04
    
df['Commision_Rate']= df['Pct_To_Target'].apply(calc_commision_rate)
    
df.head()
    
    
df['Commission_Amount']=df['Commision_Rate']*df['Sales']
 
df.head()


print(df['Sales'].sum(),df['Commission_Amount'].sum(),df['Sales_Target'].sum())

df.describe()
   
    
    