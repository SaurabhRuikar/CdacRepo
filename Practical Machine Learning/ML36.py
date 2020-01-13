#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:11:22 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/student/Desktop/Python/dataset/milk.csv')
X=df.iloc[:,1:6].values
















from sklearn.cluster import KMeans
wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=42)
y_kmeans=kmeans.fit_predict(X)

plt.scatter(X[y_kmeans==0,0],X[y_kmeans == 0,1], c= 'red',label='Cluster 1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans == 1,1], c= 'black',label='Cluster 2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans == 2,1], c= 'blue',label='Cluster 3')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroid')

plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Scores (1-100) ')
plt.legend()
plt.show()