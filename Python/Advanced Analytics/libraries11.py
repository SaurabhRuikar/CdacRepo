#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:03:18 2019

@author: student


Day 5(numpy,pandas,matplotlib,scipy)
1. Complete following program
import pandas as pd
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
# add headings to the column- col1,col2,col3,col4,col5
#display only column col3
#add col6 concatenate values of col2 and col3 and seperate them by :
# retrieve values of col1 and col4 display bar graph

# display names of all the columns.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import *

mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
#lst=['movie id','reviews','gender','job','views']
lst=['serial no','age','gender','profession','views']
mymoviedata.columns=lst
print(mymoviedata)

df=mymoviedata[['gender']]
df

df1=mymoviedata[['age']]
df1

mymoviedata['Gender : Age']=mymoviedata['gender']+":"+(mymoviedata['age'].astype(str))

#mymoviedata.drop('Gender : Job',axis=1)
mymoviedata

df2=mymoviedata['age']


df3=mymoviedata['views']
df4=mymoviedata['profession']

width=0.35
plt.bar(df2,df3,width,color='red')
plt.bar(df2,df4,width,color='red')


mymoviedata.columns




















'''
#create a list for storing year 2010 to 2014
#create a list for each year for storing sales amout 
for of 5 products in each years
#draw pie chart and stack graph to compare sales
'''



yrs=[2010,2011,2012,2013,2014]
products = {2010:[100, 200, 3000, 2500, 150],
            2011:[200, 300, 240, 350, 400],
            2012:[200, 300, 240, 350, 400],
            2013:[3200, 3300, 3240, 3350, 3400],
            2014:[2400, 2300, 1240, 340, 500]}


yr1=[100, 200, 3000, 2500, 150]
yr2=[200, 300, 240, 350, 400]
yr3=[200, 300, 240, 350, 400]
yr4=[3200, 3300, 3240, 3350, 3400]
yr5=[2400, 2300, 1240, 340, 500]



index=['TV', 'Fridge', 'AC', 'Laptop', 'Fan']
'''
df = pd.DataFrame(products,index)
cols=['g','c','m','k','b']
plt.pie(df.iloc[0],labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()


df1 = pd.DataFrame(products, index)
cols=['g','c','m','k','b']
plt.pie(df1.iloc[1],labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()


df2 = pd.DataFrame(products, index)
cols=['g','c','m','k','b']
plt.pie(df2.iloc[2],labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()


df3 = pd.DataFrame(products, index)
cols=['g','c','m','k','b']
plt.pie(df3.iloc[3],labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()

df4 = pd.DataFrame(products, index)
cols=['g','c','m','k','b']
plt.pie(df4.iloc[4],labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()

'''





m1=df[2010].max()
m2=df[2011].max()
m3=df[2012].max()
m4=df[2013].max()
m5=df[2014].max()
print(m1,m2,m3,m4,m5)


maxdf=pd.DataFrame([[m1,m2,m3,m4,m5]])
cols=['g','c','m','k','b']
plt.pie(maxdf,labels=yrs,colors=cols,startangle=90,shadow=True,explode=(0,0,0.1,0,0))
plt.show()


plt.stackplot(yrs,yr1,yr2,yr3,yr4,yr5,colors=cols)
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.show()


plt.stackplot(yrs,df[2010],df[2011],df[2012],df[2013],df[2014],colors=cols)
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.show()
