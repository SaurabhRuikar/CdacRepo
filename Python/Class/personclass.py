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

class Employee(Person):
    def __init__(self,pid=0,name="",mob="",dt="",desg=""):
        Person.__init__(self,pid,name,mob)
        self.__dept=dt
        self.__desg=desg

    def __str__(self):
        return Person.__str__(self)+"\nDepartment : "+self.__dept+"\nDesignation : "+self.__desg


    def setDept(self,dt=""):
        self.__dept=dt
        

    def setDesg(self,desg=""):
        self.__desg=desg

    def getDept(self):
        return self.__dept
 
    def getDesg(self):
        return self.__desg


class SalariedEmp(Employee):
    def __init__(self,pid=0,name="",mob="",dt="",desg="",sal=0,bonus=0):
        Employee.__init__(self,pid,name,mob,dt,desg)
        self.__sal=sal
        self.__bonus=bonus

    def __str__(self):
        return Employee.__str__(self)+"\nSalary : "+str(self.__sal)+"\nBonus : "+str(self.__bonus)

    def setSal(self,sal=""):
        self.__sal=sal
        

    def setBonus(self,bonus=""):
        self.__bonus=bonus

    def getDept(self):
        return self.__sal
 
    def getDesg(self):
        return self.__bonus

    def calcSal(self):
        da=0.10*self.__sal
        hra=0.15*self.__sal
        pf=0.08*self.__sal
        return self.__sal+da+hra-pf+self.__bonus

class Contract(Employee):
    def __init__(self,pid=0,name="",mob="",dt="",desg="",hrcharges=0,nohrs=0):
        Employee.__init__(self,pid,name,mob,dt,desg)
        self.__hrcharges=hrcharges
        self.__nohrs=nohrs

    def __str__(self):
        return Employee.__str__(self)+"\nHour Charges : "+str(self.__hrcharges)+"\nNo of Hours : "+str(self.__nohrs)

    def calcSal(self):
        return self.__hrcharges * self.__nohrs




if __name__=="__main__":    
    '''
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
    '''

    '''
    e=Employee(123,"Saurabh","323232","CDAC","Jobless")
    print(e)

    e.setDept("IT")
    print(e)
    '''

    '''
    f=SalariedEmp(123,"Saurabh","323232","CDAC","Jobless",12233,100)
    print(f)


    print(f.calculateSal())
    '''
    f=Contract(123,"Saurabh","323232","CDAC","Jobless",9999,12)
    print(f)
    print(f.calcSal())

























