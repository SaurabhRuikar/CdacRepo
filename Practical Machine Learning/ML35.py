#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:41:16 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/Mall_Customers.csv')

X=df.iloc[:,[3,4]].values


import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(X)


plt.scatter(X[y_hc==0,0],X[y_hc == 0,1],s=100, c= 'red',label='Cluster 1')
plt.scatter(X[y_hc==1,0],X[y_hc == 1,1],s=100, c= 'black',label='Cluster 2')
plt.scatter(X[y_hc==2,0],X[y_hc == 2,1],s=100, c= 'blue',label='Cluster 3')
plt.scatter(X[y_hc==3,0],X[y_hc == 3,1],s=100, c= 'yellow',label='Cluster 4')
plt.scatter(X[y_hc==4,0],X[y_hc == 4,1],s=100, c= 'green',label='Cluster 5')

plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Scores (1-100) ')
plt.legend()
plt.show()