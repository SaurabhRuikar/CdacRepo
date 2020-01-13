#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:34:08 2019

@author: student
"""
import pandas as pd
df=pd.read_csv("/home/student/Desktop/Python/dataset/weather_data.csv")

df

df.shape

df.head()

df.columns

df[['day','event']]


df['temperature'].max()

df['temperature'].std()

df.describe()

df.set_index('day')  #creates a new dataFrame and leaves the original unchanged

df.set_index('day',inplace=True) #Changes the original dataFrame

df


df.reset_index(inplace=True)

df


df.set_index('event',inplace=True)

df

#for a row or column having a specific value
df.loc['Snow']


######################################################################
#STOCK_DATA.CSV

df= pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',skiprows=1)
df

df= pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',header=1)
df

df= pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',header=None, names=['ticker','eps','revenue','people'])
df


df = pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',nrows=2)
df

df = pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',na_values=['n.a.','not available'])
df

df1= pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',na_values={'eps':['not available'],'revenue':[-1],'people':['not available','n.a.']})
df1


#write to file without indexes
df1.to_csv('/home/student/Desktop/new1.csv',index=False)
df



df2=pd.read_csv('/home/student/Desktop/new1.csv')
df2

df3=pd.read_excel('/home/student/Desktop/Python/dataset/stock_data.xlsx',"Sheet1")
df3


def convert_people_cell(cell):
    if cell=="n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell == 'n.a.':
        return 50
    return cell

df4=pd.read_excel('/home/student/Desktop/Python/dataset/stock_data.xlsx','Sheet1',converter={'people': convert_people_cell,'price': convert_price_cell})
df4



#####################################################################

#WEATHER_DATA.CSV

df1= pd.read_csv('/home/student/Desktop/Python/dataset/weather_data.csv',parse_dates=['day'])
df1

type(df1.day[0])


df = pd.read_csv('/home/student/Desktop/Python/dataset/stock_data.csv',na_values=['n.a.','not available'])
df

new_df=df.fillna(method="ffill")
new_df


df1= pd.read_csv('/home/student/Desktop/Python/dataset/weather_data.csv',parse_dates=['day'])
df1

df_new=df1.replace({'temparature':'[A-Za-z]' , 'windspeed':'[a-z]'}," " ,replace=True)
df_new
##############################################################################
#Weather by Cities csv

df= pd.read_csv('/home/student/Desktop/Python/dataset/weather_by_cities.csv')
df

g = df1.groupby('city')
g

for city,data in g:
    print('city: ',city)
    print('data : ',data)

g.get_group('mumbai')


g.max()


g.mean()


g.describe()


g.size()


g.count()


g.plot()

def grouper(df,idx,col):
    if 80<=df[col].loc[idx]<=90:
        return '80-90'
    elif 50<=df[col].loc[idx]<=60:
        return '50-60'
    elif 30<=df[col].loc[idx]<=40:
        return '30-40'
    else:
        return 'Others'
h=df.groupby(lambda x:grouper(df,x,"temperature"))
h    
for k,v in h:
    print("Group by key: {}\n".format(k))
    print(v)
    


h.plot()                             
