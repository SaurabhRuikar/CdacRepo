#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:49:39 2019

@author: student
"""
#ENSEMBLE LEARNING DEMONSTRATION


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

#GENERATING DATASET AND ADDING NOISE EXPLICITLY
X,y = make_moons(n_samples=10000,noise=.5,random_state=0)




X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)


#LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
LR=LogisticRegression(random_state=0)
LR.fit(X_train,y_train)
y_pred=LR.predict(X_test)

print("Logistic Regression : ",accuracy_score(y_test,y_pred))



#DECISION TREE CLASSIFIER TO COMPARE ACCURACY LATER WITH BOOSTING MODELS
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print("Decision Tree : ",accuracy_score(y_test,y_pred))

#RANDOM FOREST

clf=RandomForestClassifier(n_estimators=100,max_features='auto',random_state=0)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print('Random Forest : ',accuracy_score(y_test,y_pred))

#BOOSTING ALGORITHMS

#ADABOOST

clf=AdaBoostClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print('AdaBoost Classifier : ',accuracy_score(y_test,y_pred))

#GradientBoost

clf=GradientBoostingClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print('Gradient Boosting Classifier : ',accuracy_score(y_test,y_pred))

#First need to Install xgboost module
#XGBoost Classifier
from xgboost import XGBClassifier
classifier=XGBClassifier()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

print('XGBoosting Classifier : ',accuracy_score(y_test,y_pred))


