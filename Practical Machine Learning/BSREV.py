#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 09:46:32 2019

@author: student

"""

'''
import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb:mp:11ec028425&fm=neo%2Fmerchandising&iid=M_0c8da7a0-488d-4c14-a4be-405c59d99ea7_2.KJCLZLP21NP5&ppt=browse&ppn=browse&ssid=0uvhyh6lw00000001577505487667&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_KJCLZLP21NP5_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=KJCLZLP21NP5')
#print(response.content)
r_data=BeautifulSoup(response.content,'lxml')
print(r_data)
a_data=r_data.find_all('a',{'class':''})
print(len(a_data))
p_data=r_data.find_all('div',{'class':'_1vC4OE'})
rating_data=r_data.find_all('div',{'class':'hGSR34'})
cnt=0
for a,b,c in zip(a_data,p_data,rating_data):
    cnt=cnt+1
    print(str(cnt)+"."+a.get_text())
    ulink=a["href"]
    #print(ulink)
    response1=requests.get("https://www.flipkart.com"+ulink)
    r_data1=BeautifulSoup(response1.content,'lxml')
    offers=r_data1.find_all('li',{'class':'_2-n-Lg'})
    print("Numbers of offers:",len(offers))
    print("Price"+":"+b.get_text())
    print("Rating"+":"+c.get_text())
    print()


'''

	
import requests
from bs4 import BeautifulSoup
response=requests.get('http://www.know-it.co.in/Placement.aspx')
r_data=BeautifulSoup(response.content,'lxml')
print(r_data)
'''
a_data=r_data.find_all('td',{'style':"padding-left:5px;padding-right:5px"})
print(len(a_data))

for a in a_data:
    print(a.get_text())
'''

a_data=r_data.find_all('tr',{'style':"height:30px;background-color:white;padding-left:5px;padding-right:5px"})





print(len(a_data))
cnt=0
for a in a_data:
    cnt=cnt+1

   
   #n_data=a.find_all('td',{'style':"padding-left:5px;padding-right:5px"})
    c_data=a.find_all('td')
    for c in c_data:
        print(c.get_text())
print("Total Students placed :",cnt)        
        
        
    
   




