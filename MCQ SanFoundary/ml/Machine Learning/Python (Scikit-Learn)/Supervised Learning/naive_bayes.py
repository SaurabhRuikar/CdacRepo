# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:06:18 2018

@author: ss
"""

import pandas as pd

telecom = pd.read_csv("F:/Python Material/ML with Python/Datasets/Telecom.csv")

dum_telecom = pd.get_dummies(telecom, drop_first=True)

from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

X = dum_telecom.iloc[:,0:2]
y = dum_telecom.iloc[:,2]

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

bernoulli = BernoulliNB()
y_pred = bernoulli.fit(X_train, y_train).predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


multinomial = MultinomialNB()
y_pred = bernoulli.fit(X_train, y_train).predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
