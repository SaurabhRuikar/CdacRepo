#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:54:00 2019

@author: student
"""
#Decision Tree Classification
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/student/Desktop/Python/dataset/Social_Network_Ads.csv')

x = df.iloc[:,[2,3]].values
y = df.iloc[:,4].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)



from sklearn.tree import DecisionTreeClassifier


classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)



y_pred=classifier.predict(x_test)

#SVC

from sklearn.svm import SVC

clss=SVC(random_state=0)
clss.fit(x_train,y_train) 

y_pred=clss.predict(x_test)

from sklearn.model_selection import cross_val_score
score=cross_val_score(clss,x_train,y_train)
print(score)

'''

from sklearn.model_selection import cross_val_score
score=cross_val_score(classifier,x_train,y_train)
print(score.mean())
'''
from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_test,y_pred)


#Training set
from matplotlib.colors import ListedColormap
x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                  np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))


print(x_set)

plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j,0], x_set[y_set== j,1],
                c= ListedColormap(('red','green')) (i),label=j)
    
plt.title('DecisionTree(Training Set)')

plt.xlabel('Age')
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()   



#testing set
from matplotlib.colors import ListedColormap
x_set,y_set=x_test,y_test
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                  np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))


plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j,0], x_set[y_set== j,1],
                c= ListedColormap(('red','green')) (i),label=j)
    
    
plt.title('DecisionTree(Testing Set)')

plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()    




#ROC CURVE
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score    

#For Decision Tree

def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color='orange',label='ROC')
    plt.plot([0,1],[0,1],color='darkblue',linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC Curve)')
    plt.legend()
    
probs=classifier.predict_proba(x_test)

probs=probs[:, 1]

auc=roc_auc_score(y_test,probs)
print("AUC: %.2f" %auc)



fpr,tpr,thresholds=roc_curve(y_test,probs)
plot_roc_curve(fpr,tpr)    
    
  
#For SVC  

def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color='orange',label='ROC')
    plt.plot([0,1],[0,1],color='darkblue',linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC Curve)')
    plt.legend()
    
probs=clss.predict_proba(x_test)

probs=probs[:, 1]

auc=roc_auc_score(y_test,probs)
print("AUC: %.2f" %auc)



fpr,tpr,thresholds=roc_curve(y_test,probs)
plot_roc_curve(fpr,tpr)  