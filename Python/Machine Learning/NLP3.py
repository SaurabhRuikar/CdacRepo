#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:22:19 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pyfpgrowth

df = pd.read_csv('/home/student/Desktop/Python/dataset/Market_Basket_Optimisation.csv', header = None)

transactions=[]

for i in range(0,7501):
    lst=[]
    for j in range(0,20):
        if str(df.values[i,j])!='nan':
            lst.append(str(df.values[i,j]))
    transactions.append(lst)
    

print('Generating Patterns')
#function parameters = (list,support)
pattern=pyfpgrowth.find_frequent_patterns(transactions,2)

#function parameters = (generated pattern variable,min lift)
print('Generating Rules')
rules=pyfpgrowth.generate_association_rules(pattern,0.2)