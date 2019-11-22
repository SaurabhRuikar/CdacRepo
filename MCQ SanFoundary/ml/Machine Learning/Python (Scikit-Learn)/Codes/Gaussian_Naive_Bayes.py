# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:35:50 2018

@author: ss
"""

import pandas as pd

Default = pd.read_csv("F:/Python Material/ML with Python/Datasets/Default.csv")
dum_Default = pd.get_dummies(Default, drop_first=True)

from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB

X = dum_Default.iloc[:,[0,1,3]]
y = dum_Default.iloc[:,2]

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

gaussian = GaussianNB()
y_pred = gaussian.fit(X_train, y_train).predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


