#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:40:04 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Line Plot
x=[2,3,4,5,6]
y=[13,12,45,66,78]
x1=[3,7,9,2]
y2=[12,11,8,5]


plt.plot(x,y,color='r',label='Test Label')
plt.plot(x1,y2,color='b',label='Test 123')
#plt.bar(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('This is Title')
plt.legend()
plt.grid()



#Pie Chart
slices=[7,8,6,11,2]
activities=['exercises','sleeping','eating','working','playing']
cols=['g','c','m','r','k']

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0,0.5,0,0))
plt.title('1st Pie Chart')
plt.show()



#Stack Plot
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,7,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m', label="sleeping",linewidth=5)
plt.plot([],[],color='c', label="eating",linewidth=5)
plt.plot([],[],color='r', label="working",linewidth=5)
plt.plot([],[],color='b', label="playing",linewidth=5)


plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.legend(loc='upper left')
plt.title('StackPlot')
plt.show()



DayOfWeekOfCall=[1,2,3]
DispatchOnThisWeekday=[77,32,42]

LABELS=["Monday","Tuesday","Wednesday"]

width=0.35
plt.bar(DayOfWeekOfCall,DispatchOnThisWeekday,width,align='center')
plt.xticks(DayOfWeekOfCall,LABELS,rotation="45")
#plt.set_xticks(DispatchOnThisWeekday+width / 2) 
plt.show()




data={'year':[2010,2011,2012,2011,2012,2010,2011,2012],'team':['bears','bears','bears','packers','lions','lions','lions'],'wins':[11,8,10,15,11,6,10,4],'losses':[5,8,6,1,5,10,6,12]}

football=pd.DataFrame(data,columns=['year','team','wins','losses'])
print(football.head())
print('-------------------')
print(football['year'])
x=football['year']
y=football['wins']

plt.xlim(2010,2013)

plt.xticks(np.linspace(2010,2013,4,endpoint=True))

plt.ylim(2.16)

plt.yticks(np.linspace(2,16,8,endpoint=True))

plt.bar(x,y)
plt.show()





