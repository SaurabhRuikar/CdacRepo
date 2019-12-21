#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:25:51 2019

@author: student
"""

#Default.csv Dataset for checking if student is a defaulter
 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/student/Desktop/Python/dataset/Default.csv')

x = df.iloc[:,1:4].values
y = df.iloc[:,0].values


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
x[:,0]=labelencoder.fit_transform(x[:,0])
y=labelencoder.fit_transform(y)




from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(x)
X_train=sc.fit(x_train)
X_test=sc.transform(x_test)


#LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression
LR=LogisticRegression(random_state=0)
LR.fit(x_train,y_train)


from sklearn.model_selection import cross_val_score
scoreLR=cross_val_score(LR,x,y)
print(scoreLR.mean())


#SVC


from sklearn.svm import SVC

rbf=SVC(random_state=0)
rbf.fit(X,y)


linear=SVC(kernel='linear',random_state=0)
linear.fit(X,y)


poly=SVC(kernel='poly',random_state=0)
poly.fit(X,y)


scorerbf=cross_val_score(rbf,X,y)
print(scorerbf.mean())


scorelinear=cross_val_score(linear,X,y)
print(scorelinear.mean())

scorepoly=cross_val_score(poly,X,y)
print(scorepoly.mean())




#DECISION TREE
from sklearn.tree import DecisionTreeClassifier


dt=DecisionTreeClassifier(criterion='entropy',random_state=0)
dt.fit(x_train,y_train)


scoredt=cross_val_score(dt,x,y)
print(scoredt.mean())


#RANDOMFOREST TREE

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
rfc.fit(x,y)


scorerfc=cross_val_score(rfc,x,y)
print(scorerfc.mean())

#KNN

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
knn.fit(X,y)

scoreknn=cross_val_score(knn,X,y)
print(scoreknn.mean())

#NAIVE BAYES

from sklearn.naive_bayes import GaussianNB


nb=GaussianNB()
nb.fit(x_train,y_train)

scorenb=cross_val_score(nb,x,y)
print(scorenb.mean()) 


rl=scoreLR.mean()
rbf=scorerbf.mean()
ln=scorelinear.mean()
poly=scorepoly.mean()
dt=scoredt.mean()
rfc=scorerfc.mean()
knn=scoreknn.mean()
nb=scorenb.mean()
    


di={"Logistic":rl,"SVC rbf":rbf,"SVC linear":ln,"SVC Poly":poly,
"RandomForsetClassifier":rfc,"KNN":knn,"NaiveBayes":nb}


print(di)
print()
print()
aa = max(di.values())
print(aa)
for i,j in di.items():
    if aa==j:
        print(i,"has",j,"mean which is better than other algorithms")


