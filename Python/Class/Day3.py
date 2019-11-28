'''

#FOR LOOP USING ELSE (WITH BREAK CONDITION)
n=int(input("Enter the number"))

for i in range(2,n):
    if n%i==0:
        print("Not a Prime")
        break
else:
    print("Prime")


#Using sorted list for printing without changing original list.
lst=[5,7,10,20,1]
print(lst)

for i in sorted(lst,reverse=True):
#for i in sorted(lst):
    print(i,end=" ")

#Range
    
for i in range (1,10):
    print(i)


#Reversed List

lst=[5,7,10,20,1]
print(lst)

for i in reversed(lst):
    print(i,end=" ")

'''

'''

lst=[10,20,30]
lst1=["a","b","c"]
lst2=[40,50,60]

#For Output in form of tuples using only one variable
#for i in zip(lst,lst1,lst2):
#    print(i[0],i[1],i[2])


for i,j,k in zip(lst,lst1,lst2):
    print(i,j,k)

''' 

#Enumerate Function - to number beside lists

'''
lst=[10,20,30]

#Numbering/Indexing from 0
for i,j in enumerate(lst):
    print(i,j)
                                                                                                                                                                                                         
#Specifying Number/Index start by a value
for i,j in enumerate(lst,11):
    print(i,j)
'''


lst=[10,20,30,40]
lst1=["a","b","c"]

'''
for i,j in zip(enumerate(lst,11),lst1):
    print(i[0],i[1],j)


print(min(lst))
'''

#Find index of no in list without readymade fn
'''
#Using Enumerate


lst=[10,20,30,40]
n=int(input("enter the number"))
for i in enumerate(lst):
    if i[1]==n:
        print("Index is",i[0])
        break
else:
    print("Not found")



#Without Enumerate using count


lst=[10,20,30,40]
n=int(input("enter the number"))
cnt=0
for i in lst:
    
    if i==n:
        print("Index is",cnt)
        break
    cnt=cnt+1
else:
    print("Not found")

'''    


                #SETS
'''

lst=[10,20,30,40,20,20,10]
lst1=[10,10,23,45,30,20,10,20,40]

s11=set(lst)
print(s11)

s12=set(lst1)
print(s12)

s23=s11.union(s12)
print(s23)

s24=s11.intersection(s12)
print(s24)

s25=s12.difference(s11)
print(s25)


if s11<s12:
    print("Subset")
else:
    print("It is a superset")
    

print(s11.issubset(s12))

'''

'''

#Deleting From Set

s={10,20,30,40,50}
print(s)

print(s.pop())
print(s)

print(s.remove(50))
print(s)

print(s.discard(10))
print(s)
'''


'''
#Adding in Set
s=set()

ans="y"
while ans=="y":
    tree=input("enter tree")
    s.add(tree)
    ans=input("Continue")
print(s)

'''
'''

                    #FROZEN SET

s={10,20,30,40,50}
fs=frozenset(s)
print(fs)

# fs.add(50)  Not allowed as now set is immutable(FROZEN SET)

'''

'''
#SET OPERATIONS QUESTION
s1=set()
s2=set()

ans="y"
while ans=="y":
    inp=input("Enter a NUMBER (Set 1)")
    s1.add(inp)
    ans=input("Continue y/n?")


ans1="y"
while ans1=="y":
    inp1=input("Enter a NUMBER (Set 2)")
    s2.add(inp1)
    ans1=input("Continue y/n?")

print("Set 1 is ")
print(s1)
print("Set 2 is ")
print(s2)

s23=s1.union(s2)
print("Union is:")
print(s23)

s24=s1.intersection(s2)
print("Intersection is:")
print(s24)

s25=s1.difference(s2)
print("Difference is:")
print(s25)

s1.update(s2)
print(s1)
'''

'''

                #Dictionary

courses={"dbda":51,"dac":97,"dtiss":78}
courses["VLSI"]=1000

c=input("Enter course name")
t=courses.get(c,-1)
if t!=-1:
    print("Found",t)
else:
    print("Not found")

v=courses.pop("dtiss")
print(v)
print(courses)
'''

'''
#Menu Driven program for various operations on a dictionary

import sys
course={}
choice=0
while choice!=7:
    print("1. add course")
    print("2. delete course")
    print("3. update number")
    print("4. remove course")
    print("5. find course")
    print("6 find value")
    print("7. display all")
    choice=int(input("enter choice"))
    if choice==1:
            ans="y"
            while ans=="y":
                ad=input("Enter the course you want to add?")
                ad1=input("Enter Value for the above Course")
                v=course.get(ad)
                if v!=None:
                    ans1=input("Do you want to overwrite? y/n")
                    if ans1=="y":
                        course[ad]=ad1
                        print("Overwritten")
                    else:
                        print("Ignored/ Not Overwritten")
                else:
                    course[ad]=ad1
                ans=input("Do you want to continue? y/n")
                print(course)

    elif choice==2:
            ans="y"
            while ans=="y":
                ad=input("Enter the course you want to delete?")
                v=course.get(ad)
                if v!=None:
                    course.pop(ad)
                    
                else:
                    print("Already Deleted. Please Try another value")
                ans=input("Do you want to continue? y/n")
                print(course)
            
    elif choice==3:
            ad=input("Enter the course you want to update")
            v=course.get(ad)
            if v!=None:
                print(ad,"---->",v)
                nval=input("Enter new value")
                course[ad]=nval
                print("Updated Successfully")
            else:
                print("Course not found")
                    
        
        
            
    elif choice==4:
           pass
        #same as delete so not written
        
    elif choice==5:
        
            val=input("Enter the value")
            for k,v in course.items():
                if v<val:
##            for k in course.items():
##                if course[k]<val:
            
                    print(k,"---->",v)
    elif choice==6:
            cname=input("Enter course")
            val=course.get(cname,-1)
            if val!=-1:
                print(cname,"---->",val)
    elif choice==7:
            print(course)
            
    else:
            sys.exit(0)

'''
'''
#list
a=12
b=a
print(id(a))
print(id(b))
b=b+34
print(id(a))
print(id(b))
print(a,b)

lst=[10,20,30]
lst1=lst   #pointing to same object so id will be same
lst.append(12) 
print(lst)
print(lst1)
print(id(lst))
print(id(lst1))


lst1=lst.copy()#pointing to differnt object so id will be different
print(lst)
print(lst1)
print(id(lst))
print(id(lst1))
'''

'''
#set
s={10,20,30}
s1=s.copy()
print(s)
print(id(s))

print(s1)
print(id(s1))
'''





























































