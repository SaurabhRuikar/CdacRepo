#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:47:29 2019

@author: student
"""
import re
s="""Something is there somewhere with someone"""
m=re.search("t(.*?)e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
else:
    print("Not found")    
    
m=re.match("s(.*)e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.span())
    print(m.span(1))    
else:
    print("Not found")       


m=re.findall("t.*?e",s,re.I|re.M)
if m!=None:
    print(m)
else:
    print("Not found")
    

m=re.finditer("t.*?e",s,re.I|re.M)
if m!=None:
    for i in m:
        print(i.group())
        print(i.span())
else:
    print("Not found") 
    
    
m=re.sub("some","any",s,flags=re.I,count=0)
print(m)
print(s)

exp=re.compile("t.*?e",re.I|re.M)
a=exp.search(s)
print(a.group())

s = '111,user1,mon,4-11-2019, 9:00am'
#
#x = re.search("(\d{3},.+?),",s,re.I) to print user
#x=re.search(",(\d-\d{2}-\d{4})",s,re.I) to print date
#x=re.search(",((^m.*)?),",s,re.I)
print(x.group())
print(x.group(2))




    
    
    
    
    
    