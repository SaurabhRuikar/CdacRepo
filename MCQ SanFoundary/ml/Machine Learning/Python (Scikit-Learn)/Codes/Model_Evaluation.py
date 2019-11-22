# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:43:48 2018

@author: ss
"""

import numpy as np
predicted = np.array(["Y","Y","N","N","Y","N","Y","Y","N","N","N","N","Y"], 
                     dtype=object)

existing = np.array(["Y","N","N","N","Y","N","Y","N","Y","N","Y","N","Y"], 
                     dtype=object)

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(predicted, existing))
print(classification_report(predicted, existing))
