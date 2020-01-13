                    #OPERATORS
'''
a=1
b=2
d=a/b
c=a//b
print(c)
print(d)

#a/b = 0.5 but a//b =0 as it removes fractional part and only gives the positive value(FLOOR DIVISION)


print(12**3) #Power Operator


print(7<<2)  #Left Shift Operator

print(7>>2)  #Right Shift Operator

e=7
f=6
print(e&f)   #AND Operator (BITWISE OPERATOR)

'''
'''
g=e&f
x=~g

print(x)     #Wrong as of now
'''

'''
IMPORTING MATH PACKAGE

>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sqrt(144)
12.0
>>>
>>> dir(math)
>>> help(math.ceil)
Help on built-in function ceil in module math:

ceil(...)
    ceil(x)
    
    Return the ceiling of x as an Integral.
    This is the smallest integer >= x.

>>>>>> math.ceil(3.55)
4
>>> math.ceil(3.50)
4
>>> math.ceil(3.49)
4
>>> math.floor(3.49)
3
>>> math.floor(-3.45)
-4 

IMPORTING SYS AND OS PACKAGES

>>> import sys
>>> dir(sys)
>>>

>>> import os
>>> dir(os)

'''
'''

                    #SLICING 

s1="This is Testing"

print(s1[2:9])

print(s1[2:])

print(s1[:5])

print(s1[2:10:2])

print(s1[2::2])

print(s1[::-1])

print(s1[0::-1])

print(s1[::2])

print(s1[1::2])

'''

'''
>>> dir(str)
>>> "assfjkl".startswith("as")
True
>>> "jdgskhd".endswith("hd")
True
>>> "dksjldjksl".count("d")
2
>>> 


s="This is string"
pos=s1.find("is")
print(pos)

pos=s1.find("is",6)     #If string is not found after 6th position we get -1 as output.
print(pos)


pos=s1.rfind("is")      #find gives first occurence. rfind gives you the last occurence of string in your given string.
print(pos)

pos=s1.rfind("is",6)
print(pos)




                    #INDEX

pos=s1.index("is")
print(pos)

                    #STRIP function

s1="dghfft Test dghft test1 test2 ghfft"
s2=s1.strip("d ghfft")
s3=s1.rstrip("d ghfft")
s4=s1.lstrip("d ghfft")


print(s1)
print(s2)
print(s3)
print(s4)

                    #SPLIT function
#returns a list

s="jdshjdh:sjdklwjs:dsjdh,djshds"
s1=s.split(":")
print(s1)
print(type(s1))
s3="|".join(s1)   #.join() must have a list inside the parantheses and no single value
print(s3)
print(type(s3))   #will now be a string


                    #Calculating length of any Datatype
print(len(s3))
'''

'''

if "in" in "indoor Activity":
    print("Found")
else:
    print("Not found")

'''
'''
#LIST DEMO

import sys
clist=[]
choice=0
while choice!=5:
        print("1. Add in the list")
        print("2. Remove from the list")
        print("3. Seach for Position")
        print("4. Search existence")
        print("5. exit")
        choice=int(input("enter choice"))
        if choice ==1:
            ans="y"
            while ans=="y":
                city=input("Enter a city")
                clist.append(city)
                ans=input("Do you want to continue? y/n")
            print(clist)

        elif choice ==2:
            print(clist[-1])
            ans = input("Do you really want to delete it?")
            if ans=="y":
                s=clist.pop()
                print("Deleted",s,"Successfully")
                print(clist)
                
        elif choice ==3:
            

                ans=input("Enter the city that you want to search")
                if ans in clist:
                        pos=clist.index(ans)
                        print("Found at %d position" %(pos))
                        
            
        elif choice ==4:
            
                ans=input("Enter the city that you want to search")
                if ans in clist:
                    print("City exists")
                else:
                    print("City does not exist")

        
            
        else:
            sys.exit(0)
            
    
                #Tuple
a=12,13,14,"aaa" #packing of tuple
print(a)

b=(12,45,66,12,12)
print(b)
print("Length", len(b))
print("Splicing",b[0:2])
x,y,z,p=a #storing values in variables
print(x)
s=11
z=67
print(s,z)
(z,s)=s,z
print("Swapped ",s,z)
k=(34,)#To make tuple of single value
for i in b:
        if i%2==0:
                print(i)
print("count of 12 in b:",b.count(12))

'''
#LIST SORTING

lst=[12,34,45,1,23,46,78,4]
###sort ascending
##lst.sort()
##
##
##lst.sort(reverse=True) #Sorted list in reverse order
##print(lst)


lst.reverse()
print(lst)






