#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:13:43 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/student/Desktop/Python/dataset/Market_Basket_Optimisation.csv', header = None)

transactions = []

for i in range(7501):
    transactions.append([str(df.values[i, j]) for j in range(20)])
    
from apyori import apriori

rules = apriori(transactions, min_support = 0.003,
                min_confidence = 0.2, min_lift = 3, min_length = 2)

result = list(rules)

for i in result:
    print (i.items)
    