# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:43:48 2018

@author: ss
"""

import numpy as np
predicted = np.array(["Y","Y","N","N","Y","N","Y","Y","N","N","N","N","Y","N"], 
                     dtype=object)

existing = np.array(["Y","N","N","N","Y","N","Y","N","Y","Y","Y","N","Y","N"], 
                     dtype=object)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print(confusion_matrix(existing, predicted))
print(classification_report(existing, predicted))
print(accuracy_score(existing,predicted))


y_pred = np.array([13.4,45.4,89.3,90.4,87.3,45.9,16.5])
y_true = np.array([12.3,46.4,90,100.4,86.3,46,17])
from sklearn.metrics import mean_squared_error
mean_squared_error(y_true, y_pred)  


y_pred = np.array([13.4,45.4,89.3,90.4,87.3,45.9,16.5])
y_true = np.array([12.3,46.4,90,100.4,86.3,46,17])
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_true, y_pred)  

y_pred = np.array([13.4,45.4,89.3,90.4,87.3,45.9,16.5])
y_true = np.array([12.3,46.4,90,100.4,86.3,46,17])
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)  
