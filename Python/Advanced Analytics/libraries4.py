#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:15:31 2019

@author: student
"""

#pandas continuation


import numpy as np
import pandas as pd

Data={'Product':['AAA','BBB','CCC'],'Price':['210','250','22XYZ']}

df=pd.DataFrame(Data)
df['Price']=pd.to_numeric(df['Price'],errors='coerce')
print(df)
print(df.dtypes)
df['Price']=df.replace(np.NaN,0,regex=True)
df['Price']=df['Price'].astype(int)
print(df)


Data={'name':['Jason','Molly','Tina','Jake','Amy'],'year':[2012,2012,2013,2014,2014],'reports':[4,24,31,2,3]}

df=pd.DataFrame(Data,index=['Cochice','Pima','Santa Cruz','Maricopa','Yuma'])

df


df.drop()
