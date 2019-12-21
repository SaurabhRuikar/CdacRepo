#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:27:15 2019

@author: student
"""

import numpy as np
import pandas as pd


dataset=pd.read_csv('/home/student/Desktop/Python/dataset/Social_Network_Ads.csv')
X=dataset.iloc[:,[2,3]].values
Y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

d = {}

###1
from sklearn.linear_model import LogisticRegression
classifier1 = LogisticRegression(random_state=0)
classifier1.fit(x_train,y_train)

from sklearn.model_selection import cross_val_score
score1=cross_val_score(classifier1,x_train,y_train,cv=5)
#print(score1)
avg1=np.average(score1)
print("Logistic Regression Score :",avg1)
#print(score1.mean())

d["Logistic Regression Score :"] = avg1


###2
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train1=sc.fit_transform(x_train)
x_test1=sc.fit_transform(x_test)

from sklearn.svm import SVC
classifier2=SVC(kernel='linear',random_state=0)
classifier2.fit(x_train1,y_train)

score2=cross_val_score(classifier2,x_train1,y_train,cv=5)
#print(score2)
avg2=np.average(score2)                 
print("SVR Linear Score:",avg2)    

d["SVR Linear Score:"] = avg2

#####3

from sklearn.svm import SVC
#classifier=SVC(kernel='rbf',random_state=0)
classifier3=SVC(kernel='poly',degree=2,random_state=0) ## by default degree=3
classifier3.fit(x_train1,y_train)

score3=cross_val_score(classifier3,x_train1,y_train,cv=5)
#print(score2)
avg3=np.average(score3)                 
print("SVR Kernel(poly) Score:",avg3)    

d["SVR Kernel(poly) Score:"] = avg3

from sklearn.svm import SVC
classifier3=SVC(kernel='rbf',random_state=0)
classifier3.fit(x_train1,y_train)

score31=cross_val_score(classifier3,x_train1,y_train,cv=5)
print(score2)
avg31=np.average(score31)                 
print("SVR Kernel(rbf) Score:",avg31)    

d["SVR Kernel(rbf) Score:"] = avg31

######4

from sklearn.tree import DecisionTreeClassifier
classifier4=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier4.fit(x_train,y_train)

score4=cross_val_score(classifier4,x_train,y_train,cv=5)
#print(score4)
avg4=np.average(score4)
print("Decesion Tree Score:",avg4)

d["Decesion Tree Score:"] = avg4
#######5
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)

score5=cross_val_score(classifier,x_train,y_train,cv=5)
#print(score1)
avg5=np.average(score5)
print("Random Forest Score:",avg5)

d["Random Forest Score:"] = avg5
#####6

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(x_train1,y_train)

from sklearn.model_selection import cross_val_score
score6=cross_val_score(classifier,x_train1,y_train,cv=5)
#print(score6)
avg6=np.average(score6)
print("KNN Score:",avg6)
d["KNN Score:"] = avg6

#####7

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)

from sklearn.model_selection import cross_val_score
score7=cross_val_score(classifier,x_train,y_train,cv=5)
#print(score6)
avg7=np.average(score7)
print("Naive Bays Score:",avg7)

d["Naive Bays Score:"] = avg7

#print(d)

m = max(d.values())

for i in d.items():
    if i[1] == m:
        print('-------------------------------------------------------')
        print(i[0],i[1])





