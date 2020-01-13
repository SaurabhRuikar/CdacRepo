#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:24:33 2019

@author: student
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/student/Desktop/survey.csv')
df


age=df['Age']
age
mean=age.mean()
print("Mean ",mean)
median=age.median()
print('Median ',median)
mode=age.mode()
#print(type(mode))
print('Mode ',mode.values[0])

print('Mean: ',mean,'\nMedian: ',median,'\nMode: ',mode.values[0])
plt.figure(figsize=(10,5))
plt.hist(age,bins=15,color='grey')
plt.axvline(mean,color='red',label='Mean')
plt.axvline(median,color='yellow',label='Median')
plt.axvline(mode.values[0],color='green',label='Mode')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()




age.min()

age.max()

age.max()-age.min()


age.std()

age.var()

q1=age.quantile(0.25)
q1

q2=age.quantile(0.5)
q2

q3=age.quantile(0.75)
q3

IQR=q3-q1
IQR

plt.boxplot(age)
plt.show()



#to generate random variables
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform,norm,gamma,expon,poisson,binom

n=10000

start=10
width=20

data_uniform=uniform.rvs(size=n,loc=start,scale=width)

ax=sns.distplot(data_uniform,bins=100,kde=True,
                color='brown',
                hist_kws={'linewidth':15,'alpha':1})

ax.set(xlabel='Uniform Distribution',ylabel='Frequency')





data_normal=norm.rvs(size=10000,loc=0,scale=1)

ax=sns.distplot(data_normal,bins=100,kde=True,color='skyblue',
                hist_kws={'linewidth':15,'alpha':1})
ax.set(xlabel='Normal Distribution',ylabel='Frequency')



data_gamma=gamma.rvs(a=5,size=10000)

ax=sns.distplot(data_gamma,kde=True,bins=100,color='red',
                hist_kws={'linewidth':15,'alpha':1})



data_expon=expon.rvs(scale=1,loc=0,size=1000)

ax=sns.distplot(data_expon,bins=100,kde=True,color='skyblue',
                hist_kws={'linewidth':15,'alpha':1})



data_poisson=poisson.rvs(mu=3,size=10000)

ax=sns.distplot(data_poisson,bins=30,kde=False,color='black',hist_kws={'linewidth':15,'alpha':1})

ax.set(xlabel='Poisson Distribution',ylabel='Frequency')




data_binom=binom.rvs(n=10,p=0.8,size=10000)

ax=sns.distplot(data_binom,
                bins=30,
                kde=False,
                color='black',
                hist_kws={'linewidth':15,'alpha':1})
ax.set(xlabel='Binomial Distribution',ylabel='Frequency')


 
#Probablity Mass Function

numthrows=10000
outcomes=np.zeros(numthrows)
for i in range(numthrows):
    outcome=np.random.choice(['1','2','3','4','5','6'])
    outcomes[i]=outcome
val,cnt=np.unique(outcomes,return_counts=True)
prop=cnt/len(outcomes)
plt.bar(val,prop)
plt.ylabel("Probablity")
plt.xlabel("Outcome")
plt.show()
plt.close()

