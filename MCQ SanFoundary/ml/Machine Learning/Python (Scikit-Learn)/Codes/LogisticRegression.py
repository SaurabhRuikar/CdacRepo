# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 18:37:40 2018

@author: ss
"""
import pandas as pd
import numpy as np

Default = pd.read_csv("F:/Python Material/ML with Python/Datasets/Default.csv")
dum_Default = pd.get_dummies(Default, drop_first=True)

## Consider Student variable
X=pd.DataFrame(dum_Default['student_Yes'])
y = dum_Default.iloc[:,2]

# Import the necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report

logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X,y)

### Predicting categorical values
trialvals = np.array([0,1])
X_test = pd.DataFrame(trialvals)
logreg.predict_proba(X_test)

## Consider Income variable
X=pd.DataFrame(dum_Default['income'])
y = dum_Default.iloc[:,2]

# Import the necessary modules

logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X,y)

### Predicting numeric values
trialvals = np.array([10000,30000,50000,70000])
X_test = pd.DataFrame(trialvals)
logreg.predict_proba(X_test)
logreg.coef_
logreg.intercept_


X = dum_Default.iloc[:,[0,1,3]]
y = dum_Default.iloc[:,2]
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, 
                                                    random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()
# Fit the classifier to the training data
logreg.fit(X_train,y_train)
# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)
# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


################ROC#############################

# Import necessary modules
from sklearn.metrics import roc_curve, roc_auc_score

# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:,1]

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
import matplotlib.pyplot as plt
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
roc_auc_score(y_test, y_pred_prob)
