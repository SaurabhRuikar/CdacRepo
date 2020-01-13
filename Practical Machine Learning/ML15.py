#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:33:08 2019

@author: student
"""

#MONTE CARLO
import numpy as np
import pandas as pd


d=pd.read_csv('/home/student/Desktop/Python/dataset/clinic.csv')

k=d['No of Patients'].sum()

d['Probability']=d['No of Patients'].map(lambda x:x/k)


    
l=len(d['Probability']) 
print(l)
z=0

d['Cumulative frequency']=d['Probability'].cumsum()

l = [0,40,55,70,80]
u= [39,54,69,79,99]
d['Lower Limit']= pd.DataFrame(l)
d['Upper Limit']= pd.DataFrame(u)