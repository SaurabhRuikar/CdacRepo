#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:36:03 2019

@author: student
"""

import pandas as pd

mydata=pd.read_table('/home/student/Desktop/dataset/Chiporder.dat')
print(mydata.columns)


mymoviedata=pd.read_table('http://bit.ly/movieusers', sep='|',header=None)
print(mymoviedata.columns)

print(mydata.shape)
print(mymoviedata.shape)

print(mydata.head())
print(mydata.tail())


print(mymoviedata.head())
print(mymoviedata.tail())

print(mydata.iloc[1:5,2])
print(mydata.loc[1:5,'item_name']) #when column name is used.

df=mydata.loc[(mydata["item_name"]=="Chicken Bowl"),["item_name","quantity"]]
print(df)


lst=['movie id','reviews','gender','job','views']
mymoviedata.columns=lst
print(mymoviedata)


'''
ERROR

ds=print(mymoviedata.loc[(mymoviedata['views']>=32000),['gender','job','views']])
print(ds)
'''

ds=print(mymoviedata.loc[(mymoviedata['gender']=='M'),['gender','job','views']])
print(ds)


print(mydata.info())

dx=mydata.loc[(mydata['quantity']>1),['quantity','item_name']]
print(dx)

print(mydata.describe())
print(mymoviedata.info())


g=mymoviedata.loc[(mymoviedata['reviews']>20 and  mymoviedata['job']=='technician'),['movie id','reviews','job']]
print(g)

mymoviedata['job length']=mymoviedata['job'].map(lambda x : len(x))             

dummy_data1={'id':['1','2','3','4','5'],'Feature1':['A','C','E','G','I'],'Feature2':['B','D','F','H','J']}

df1=pd.DataFrame(dummy_data1,columns=['id','Feature1','Feature2'])
df1

dummy_data2={'id':['1','2','6','7','8'],'Feature1':['K','M','O','Q','S'],'Feature2':['L','N','P','R','T']}

df2=pd.DataFrame(dummy_data2,columns=['id','Feature1','Feature2'])
df2

df1['dept']='sales'
df2['dept']='Purchase'
combined=pd.concat([df1,df2],ignore_index=True)
combined


dummy_data3={'id':['1','2','6','7','8'],'Feature3':[12,13,14,15,16]}
df3=pd.DataFrame(dummy_data3,columns=['id','Feature3'])
df3


df_merge=pd.merge(combined,df3,on='id')
df_merge


c=mymoviedata.groupby('job').count()
print(c)


d=mymoviedata.groupby('job').first()
print(d)


t=mymoviedata.groupby('job')
p=t.get_group('technician')


print(mymoviedata['job'].unique())




































