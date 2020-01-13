#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:34:32 2019

@author: student
"""
import pandas as pd


#reading file and parsing date into date format
df= pd.read_csv('/home/student/Desktop/Python/dataset/aapl.csv',parse_dates=['Date'])
df

#First 5 largest values in Volume Column
df.nlargest(5,'Volume',keep='first')

#Displaying Year 
df['Year']=[d.year for d in df.Date]
df

#Displaying Month
df['Month']=[d.strftime('%b') for d in df.Date]
df

#Using Slicing for retrieving only specific no of rows
df2=df[:3]
df2

#Drop newly created Year Column
df3=df.drop('Year',axis=1)
df3

#Setting Month Column as a Index
df3.set_index('Month',inplace=True)
df3

#Displaying all values for Specific Month July
df3.loc['Jul']

#Putting Index back to original 
df3.reset_index(inplace=True)
df3


#Writing to a csv file and not incuding Indexes
df3.to_csv('/home/student/Desktop/practice.csv',index=False)


#####################################################################
#Reading Another file 
df=pd.read_csv('/home/student/Desktop/survey.csv')
df

#Using forward fill in fillna function to replace NaN values
new_df=df.fillna(method='ffill')
new_df

#Using backward fill in fillna function to replace NaN values
new_df1=df.fillna(method='bfill')
new_df1

#Using Interpolate Function to add values in NaN which are equidistant from the previous and next values
new_df2=df.interpolate()
new_df2

#Using forward fill with fillna and limiting it to only 1 value. so only 1 value will be changed from NaN to something else.
new_df3=df.fillna(method='ffill',limit=1)
new_df3

#Replacing list of values with a single value
new_df4=df.replace(to_replace=[18.5,16.3],value=6767)
new_df4

#grouping data on Smoke Column
g=df.groupby('Smoke')
g

#iterating and displaying groups
for k,v in g:
    print("Smoke: ",k)
    print("\n")
    print("DATA",v)
    
#size 
g.size()

#Using gplot to display graphs
g.plot()

#Describe function to display various values such as min,max,std etc
g.describe()

g.count()

#getting data for a specific group
g.get_group('Heavy')

def grouper(df,idx,col):
    if 10<=df[col].loc[idx]<=15:
        return '10-15'
    elif 16<=df[col].loc[idx]<=20:
        return '16-20'
    elif 21<=df[col].loc[idx]<=25:
        return '21-25'
    elif 26<=df[col].loc[idx]<=30:
        return '26-30'
        
f=df.groupby(lambda x:grouper(df,x,'NW.Hnd'))
for k,v in f:
    print("Group: ",k)
    print("\n")
    print("DATA",v)