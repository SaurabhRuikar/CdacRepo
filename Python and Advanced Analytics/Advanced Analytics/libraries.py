#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:32:29 2019

@author: student
"""
     #Numpy
import numpy as np
a=np.array([1,2,3,4.0])
b=np.array([(1.5,2,3),(4,5,6)])
c=np.array([[1,2],[3,4]],dtype=complex)
print(b)
print(c)
print(a)
print(a.ndim)
print(a.shape)


print(a.dtype)
print(a.itemsize)
print(a.data)

x=np.zeros((3,4))
print(x)

y=np.ones((2,3,4),dtype=np.int16)
print(y)


b=np.arange(12).reshape(2,6)
print(b)

c=np.arange(24).reshape(2,2,6)
print(c)



w=np.array([20,30,40,50])
print(w)
v=np.arange(4)
print(v)

c = w-v
print(c)

print(v**2)

print(10*np.sin(w))




A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])

print(A*B)

print(A.dot(B))

print(np.dot(A,B))

s=np.ones((2,3),dtype=int)

s *= 3

C=np.random.random((2,3))
print(C)

C += s

#s += C

print(C)
print(s)





p=np.array([[2,8],[2,4],[5,8],[9,1]])
print(p)
p.resize((2,4))
print(p)
x=np.random.normal()
print(x)

r=np.random.normal(size=4)
print(r)

print(np.random.randint(low=1,high=10000,size=4))



a=np.eye(4,4,k=0,dtype=int)
print(a)
print()
b=np.eye(4,4,k=-1,dtype=int)
print(b)
print()

c=np.eye(4,4,k=-2,dtype=int)
print(c)

print()

print(np.identity(4))











a=np.arange(28).reshape(7,4)
#print(a)


for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
    
print(a)

b=np.arange(3,15,4).reshape(3,1)
print(b)

a=np.arange(12).reshape(3,4)
for x,y in np.nditer([a,b]):
    print(x,y)
    





                            #PANDAS
    
    
import pandas as pd

s=pd.Series(np.random.randn(5), index=['a','b','c','d','e'])

print(s)

print(s.index)
    
print(s[:3])    
    
   


d={'b':1,'a':4,'c':7}

print(pd.Series(d)) 
    
print(pd.Series(5.,index=['a','b','c','d','e']))



print(s[s>s.median()])

print(s[s> s.mean()])
print(s[[4,3,1]])
print(np.exp(s))
print(s['a'])

print('a' in s)
print(s.get('z',np.nan))


print(s+s)

print(s * 5)






print(s)



























    
    















