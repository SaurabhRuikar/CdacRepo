#inet addr:192.168.1.34 PC IP


                    #FUNCTIONS

#WE USE KEYWORD DEF FOR DEFINING FUNCTIONS
#never print values in functions as far as possible. Use return statements instead.
'''
import sys
#Prime no Check


def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return True
            break
    else:
        return False


#Simple Interest

def simple(p,n):
    r = 0.06
    return (p * n * r)/100

#Pattern Triangle
def triangle(n):
    for i in range(1,n+1):
        '''
'''
        if i == 1:
            print(i)
        else:
            print(i,i*1)
        '''
'''
        print("{} ".format(i)*i)

print("1. Prime")
print("2. Simple Interest")
print("3. Display Triangle")
print("4. Exit")

choice=int(input("Enter Choice"))
if choice ==1:
    num = int(input("Enter no"))
    ans = prime(num)
    if ans:
        print("No is not prime")
    else:
        print("No is prime")

elif choice ==2:
    p=float(input("Enter number"))
    n=int(input("Enter number"))
    interest=simple(p,n)
    print("Interest : ",interest)

elif choice == 3:
    n=int(input("Enter no"))
    tri=triangle(n)

else:
    sys.exit(0)


'''

'''
#Returning Multiple Values

def func(a,b):
    a = a + 10
    b = b + 20
    return a,b

ans = func(10,20)
print(ans)
print(type(ans))        #Returns a Tuple

#Most other languages do not allow returning multiple values like this.

'''

                #Using Default Parameters
'''
def func(a,b=5):
    a = a + 10
    b = b + 20
    return a,b

ans = func(10)
print(ans)

'''

#During default parameters either give values for all default parameters or else give values for all/others other than the left most parameter.
# def func(a=10,b) will give error but def func(a=10,b=10) or def func(a,b=10) wont give error.  
'''
def func(a=10,b=5):
    a = a + 10
    b = b + 20
    return a,b

ans = func()
print(ans)
'''

'''
ERROR (NON DEFAULT ARGUMENT IS FOLLOWED BY A DEFAULT ARGUMENT)

def func(a=10,b):
    a = a + 10
    b = b + 20
    return a,b

ans = func(10)
print(ans)
'''

'''
#THIS IS ALSO ALLOWED
def func(a=1,b=1):
    a = a + 10
    b = b + 20
    return a,b

ans = func(10,10)
print(ans)
'''

'''
#VARIABLE PARAMETERS. THE *T IS A TUPLE SO IT CAN BE ITERATED. HERE WE USE IT FOR CALCULATING SUM OF ALL VALUES IN *T.
def f1(a=1,b=1,c=10,*t):
    s=a+b+c
    for i in t:
        s=s+i
    return s

s=f1(10,20)
print(s)
s=f1()
print(s)
s=f1(23)
print(s)
s=f1(12,34,56)
print(s)
s=f1(10,20,30,40,50,60,70,80)
print(s)
'''

'''
#Keyword arguments parameter. **kwarg means dictionary. the name kwarg can be replaced with any other name. The importance is the no of *'s. 1 star gives tuple. 2 gives dictionary

def f1(a=1,b=1,c=10,**kwarg):
    s=a+b+c
    for i in kwarg.values():
        s=s+i
    return s

s=f1(10,20)
print(s)
s=f1()
print(s)
s=f1(23)
print(s)
s=f1(12,34,56)
print(s)
s=f1(10,20,30,x=40,y=50,z=60)
print(s)

#Keys in kwargs should not match names with the normal defined paramaters outside kwargs
'''

'''
#We can also use combination of variable parameters and keyword argument parameters


def f1(a=1,b=1,c=10,*t,**kwarg):
    s=a+b+c
    for n in t:
        s=s+n
    for i in kwarg.values():
        s=s+i
    return s



s=f1(10,20,30,40,50,60,70,x=10,y=20,z=30)
print(s)
'''

'''

#We can also break sequence of assigning values
#Useful when we have a lot of compulsory parameters 


def f1(a,b):
    print(a)
    print(b)

f1(b=10,a=33)
'''


                #Built In Functions

#Call by reference
'''
lst=[]
def addlst(x,l):
    l.append(x)

addlst(5,lst)
print(lst)
'''


                #Lambda Functions

'''
#FILTER FUNCTION

lst1=[]
lst=[5,10,3,3,15,2,100]

lst1=list(filter(lambda x : x % 5 == 0,lst))
print(lst1)
'''

#Reduces code. No need for loop.
#Filter itself does not return a list. It needs to be converted into a list!

'''
#Q1 WAP in python to find all values which are divisible by 5 and are greater than 6

lst1=[]
lst=[5,10,3,3,15,2,100]

lst1=list(filter(lambda x : x % 5 == 0 and x > 6,lst))
print(lst1)
'''

'''
#MAP FUNCTION

lst1=[]
lst=[5,10,3,3,15,2,100]

lst1=list(map(lambda a : a*a,lst))
print(lst1)
'''

#Difference between map and filter function
#Filter function will always give you existing original value.
#Map function gives you a new value depending upon your operation.
#During condition questions use filter.


'''
#REDUCE FUNCTION

lst=[5,7,2,10]

from functools import reduce
s=reduce(lambda x,y : x+y,lst)
print(s)


#REDUCE RETURNS ONLY 1 VALUE SO WE DONT NEED TO CONVERT INTO LIST. IF WE DO THEN WE GET THE FOLLOWING ERROR.

#lst1=list(reduce(lambda x,y : x+y,lst))
#TypeError: 'int' object is not iterable
'''

'''
#Shortcut For Loop(FILTER)
lst1=[]
lst=[5,7,2,10]

lst1=[x for x in lst if x % 5 == 0]
print(lst1)


#Shortcut For Loop(MAP)
lst1=[]
lst=[5,7,2,10]

lst1=[a*a for a in lst]
print(lst1)
'''


'''
#SORTING on 1st value of tuple in list
lst=[(1,"one"),(2,"two"),(3,"three"),(0,"zero")]

lst.sort()
print(lst)

#SORTING on 2nd value of tuple in list

lst=[(1,"one"),(2,"Two"),(3,"three"),(0,"zero")]

lst.sort(key=lambda x : x[1])
print(lst)

#since Capital letters have lower ascii value, the output will have all capital letter tuples before the smaller letter ones.
'''



#Generalized approach for question in book
#Create a list to store some values and generate another lost and the new list should contain values by adding 10 in each value of lst1.

'''
def f1(n):
    return lambda x : x + n

lst=[5,10,15,20,25]
lst1=[]

lst1=list(map(f1(10),lst))
print(lst1)
'''

#Non Generalized approach
'''
lst=[5,10,15,20,25]
lst1=[]

lst1=list(map(lambda x : x+10,lst))
print(lst1)
'''


#Program to add and delete data (menu driven)
import sys

def addList(num,lst):
    if num>=10 and num<=30:
        lst.append(num)
        return True
    else:
        return False

def delList(num,lst):
    lst.remove(num)

def searchList(num,lst):
    for i in lst:
        if num==i:
            #print("Found")
            return True
        else:
            #print("Not Found")
            return False

def modifyList(num,lst):

    if num in lst:
        num1=int(input("Enter new number to replace old no"))
        x=lst.index(num)
        
        lst[x]=num1
        return True

    else:
        return False         

lst=[]
choice=0

while choice != 5:    
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Search Data")
    print("4. Modify Data")
    print("5. exit")
    choice=int(input("Enter choice"))
    if choice ==1:

        ans="y"
        while ans=="y":
            num=int(input("Enter num"))
            if num>=10 and num<=30:
                addList(num,lst)
                print("Added Successfully")
                print(lst)
            else:
                print("Sorry pls check range! (Range 0-30)");
            ans=input("Do you want to continue? y/n")

    elif choice ==2:
        
        ans="y"
        while ans=="y":
            num=int(input("Enter num to be deleted"))
            if num in lst:

                delList(num,lst)
                print("Deleted Successfully")
                print(lst)
                
            else:
                print("Num not found")
                ans=input("Do you want to continue? y/n")

    elif choice ==3:

        ans="y"
        while ans=="y":
            num=int(input("Enter num to be searched"))

            op=searchList(num,lst)
            if op:
                print("Found")
            else:
                print("Not Found")
            
            print(lst)

            ans=input("Do you want to continue? y/n")
            
    
    elif choice ==4:

        ans="y"
        while ans=="y":
            num=int(input("Enter num to be modified"))


            y=modifyList(num,lst)

            if y:
                 print(" Successfully Replaced")
                 print(lst)
            else:
                 print("Number not found. Try Again")

            ans=input("Do you want to continue? y/n")
        
        
    else:
        sys.exit(0)












