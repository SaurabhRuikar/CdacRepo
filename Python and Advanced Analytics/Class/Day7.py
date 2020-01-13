                    #Multiple Inheritance
'''
class A:
    def __init__(self,a1=0,a2=0):
        self.a1=a1
        self.a2=a2
    def __str__(self):
        return "A1: "+str(self.a1)+" A2: "+str(self.a2)
class B:
    def __init__(self,b1):
        self.b1=b1
    def __str__(self):
        return " B1: "+str(self.b1)
class C(A,B):
    def __init__(self,a1=0,a2=0,b1=0,c1=0,c2=0):
        A.__init__(self,a1,a2)
        B.__init__(self,b1)
        self.c1=c1
        self.c2=c2
    def __str__(self):
        return A.__str__(self)+B.__str__(self)+" c1: "+str(self.c1)+" c2: "+str(self.c2)

ob=C(10,20,30,40,50)
print(ob)
'''
                #HYBRID Inheritance

'''
class A:
    def __init__(self,a1,a2):
        print("A Init Called")
        self.a1=a1
        self.a2=a2

    def __str__(self):
    
        return "A1 : "+str(self.a1)+" A2 : "+str(self.a2)
    
class B(A):
    def __init__(self,b1,**kv):
        print("B Init Called")
        super().__init__(**kv)
        self.b1=b1

    def __str__(self):
        return super().__str__()+" B1 : "+str(self.b1)

class C(A):
    def __init__(self,c1,c2,**kv):
        print("C Init Called")
        super().__init__(**kv)
        self.c1=c1
        self.c2=c2

    def __str__(self):
        return super().__str__()+" C1 :"+str(self.c1)+" C2 : "+str(self.c2)


class D(B,C):
    def __init__(self,d1,d2,**kv):
        print("D Init Called")
        super().__init__(**kv)
        self.d1=d1
        self.d2=d2

    def __str__(self):
        return super().__str__()+" D1 : "+str(self.d1)+" D2 : "+str(self.d2)

'''


'''
ob=D(d1=10,a1=20,a2=15,b1=5,c1=3,c2=7,d2=9)
print(ob)
'''

'''
oj=D(10,20,a1=15,a2=5,b1=3,c1=7,c2=9)
print(oj)
''' 

'''
NOT POSSIBLE (Gives multiple values to d1)

oj=D(3,d1=10,d2=0,a1=15,a2=5,c1=7,c2=9)
print(oj)

Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day7.py", line 79, in <module>
    oj=D(3,10,d2=0,a1=15,a2=5,c1=7,c2=9)
TypeError: __init__() got multiple values for argument 'd2'
'''

'''
class Dog:
    kind="canine"
    def __init__(self,name):
        self.name=name

d=Dog('Fido')
e=Dog('Buddy')
print(d.kind)
print(e.kind)
'''

'''
class Dog:
    def __init__(self,name):
        self.name=name
        self.tricks=[]

    def add_trick(self,trick):
        self.tricks.append(trick)


d=Dog('Fido')
e=Dog('Buddy')
d.add_trick('play dead')
e.add_trick('dead')
print(d.tricks)
print(e.tricks)
'''

'''
class A:
    def hello(self):
        print("Hello, I'm A")

#class B(A):
#    pass


class B(A):
    def hello(self):
        print("Hello, I'm B")
a=A()
b=B()

a.hello()
b.hello()
'''        

'''
from abc import ABC,abstractmethod
#abc is a inbuilt class and thus no need to create it. 

class AbstractClassExample(ABC):
    def __init__(self,value):
        self.value=value
        super().__init__()
        
    @abstractmethod
    def do_something(self):
        pass
    
  
class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value+42
    
    
class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value*42
    
    
    
x=DoAdd42(10)
y=DoMul42(10)

print(x.do_something())
print(y.do_something())
'''


#Exception Handling

'''
for i in range(3):
    try:
        n=int(input("Enter the no"))
        print(n)
        x=int(input("Enter the number"))
        test={"a":321,"b":345,"c":343}
        print(test["c"])
        d=n/x
        print(d)
        break
        
        
    except ValueError:
        print("Enter the integer")
        
    except ZeroDivisionError:
        print("pls enter non zero number")
    except KeyError:
        print("key not found")
    except:
        print("Error occured")


    finally:
        print("In finally Block")

else:
    print("Pls contact your admin")
    
'''  
for i in range(3): 
    try:
    
        n1=int(input("Enter number"))
        n2=int(input("Enter the second number"))
        
        if n2==0:
            raise ZeroDivisionError("Number is zero")  
            
        d=n1/n2
        print(d)
        break
    
    except ZeroDivisionError as e:
        print(e)
               
            
        



























 



        


    





        

        
