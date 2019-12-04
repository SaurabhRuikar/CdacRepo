            #OBJECT ORIENTED PROGRAMMING
'''
class Point:
    def __init__(self,a=0,b=0):
        print("Init called")
        self.__x=a
        self.__y=b

    def __add__(self,s):
        if isinstance(s,Point):
            a=self.__x+s.__x
            b=self.__y+s.__y
        else:
            a=self.__x+s
            b=self.__y+s
##        a=self.__x+self.__y
##        b=s.__x+s.__y
        return Point(a,b)

    000

    def __radd__(self,s):
         a=self.__x+s
         b=self.__y+s
         return Point(a,b)     
        
    

    def __sub__(self,s):
        p=self.__x-s.__x
        q=self.__y-s.__y
        return Point(p,q)
    
    def __mul__(self,s):
        p=self.__x*s.__x
        q=self.__y*s.__y
        return Point(p,q)

    def __truediv__(self,s):
        p=self.__x/s.__x
        q=self.__y/s.__y
        return Point(p,q)
    
    def __str__(self):
        print("Str Called")
        return "x : "+str(self.__x)+" y: "+str(self.__y)




p=Point(30,50)
q=Point(10,10)
print(p)
print(q)
a=p+q
print(a)
c=p-q
print(c)
d=p*q
print(d)
e=p/q
print(e)
f=p+20
print(f)
g=20+p
print(g)
'''

class Person:
    count=0                         #static variable
    def __init__(self,pid=0,name="",mob=""):
        Person.count=Person.count+1
        self.__pid=pid
        self.__name=name
        self.__mob=mob
        
    def __str__(self):
        return "Id : "+str(self.__pid)+"\nName : "+str(self.__name)+"\nMobile : "+str(self.__mob)

#Setters
    
    def setMob(self,m=""):
        self.__mob=m

    def setName(self,n=""):
        self.__name=n

    def setPid(self,o=""):
        self.__pid=o

#Getters
        
    def getMob(self):
        return self.__mob
    
    def getName(self):
        return self.__name

    def getPid(self):
        return self.__pid
    
    
if __name__ == "__main__":    
    p=Person(123,"Saurabh","88888888888")
    q=Person(129,"Ankit","77777777777")

    print(p)
    print(p.count)
    print(q)
    print(q.count)

    print()
    print("After Modifications")
    print()

    p.setMob("989898989898")
    print(p)

    q.setName("Sankalpa")
    print(q)

































