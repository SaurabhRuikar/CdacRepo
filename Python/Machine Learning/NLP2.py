#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:32:35 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re

df=pd.read_csv('/home/student/Desktop/Python/dataset/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
corpus=[]

for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ',df['Review'][i])
    review=review.lower()
    
    review=review.split()
    #By default split by tab
    
    ps = PorterStemmer()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]

    review=' '.join(review)
    corpus.append(review)


#Creating bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()
y=df.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

                            #Naive Bayes

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy-73%
accuracy=(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print(accuracy)

#Precision-68%
precision=(cm[1,1])/(cm[1,1]+cm[0,1])
print(precision)

#Recall-88%
recall=(cm[1,1])/(cm[1,1]+cm[1,0])
print(recall)

#f1 Score 
fscore=(2*precision*recall)/(precision+recall)
print(fscore)
#f1 Score = 0.77

                           #Decision Tree

from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(criterion='entropy',random_state=0)
dt.fit(X_train,y_train)

y_pred=dt.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy-71%
#Precision-74%
#Recall-66%
#f1 Score = 0.69


accuracy=(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print(accuracy)

precision=(cm[1,1])/(cm[1,1]+cm[0,1])
print(precision)


recall=(cm[1,1])/(cm[1,1]+cm[1,0])
print(recall)

 
fscore=(2*precision*recall)/(precision+recall)
print(fscore)




                          #RANDOM FOREST TREE

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
rfc.fit(X_train,y_train)

y_pred=rfc.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy-72%
#Precision-85%
#Recall-55%
#f1 Score = 0.66 

accuracy=(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print(accuracy)

precision=(cm[1,1])/(cm[1,1]+cm[0,1])
print(precision)

recall=(cm[1,1])/(cm[1,1]+cm[1,0])
print(recall)


fscore=(2*precision*recall)/(precision+recall)
print(fscore)



                        #BernoulliNB
                        
from sklearn.naive_bayes import BernoulliNB
classifier=BernoulliNB()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy-77%
#Precision-77%
#Recall-78%
#f1 Score = 0.77



accuracy=(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print(accuracy)

precision=(cm[1,1])/(cm[1,1]+cm[0,1])
print(precision)

recall=(cm[1,1])/(cm[1,1]+cm[1,0])
print(recall)

#f1 Score 
fscore=(2*precision*recall)/(precision+recall)
print(fscore)



                        #KNN
                        
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy-61%
#Precision-67%
#Recall-46%
#f1 Score = 0.54


accuracy=(cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
print(accuracy)


precision=(cm[1,1])/(cm[1,1]+cm[0,1])
print(precision)


recall=(cm[1,1])/(cm[1,1]+cm[1,0])
print(recall)

 
fscore=(2*precision*recall)/(precision+recall)
print(fscore)

