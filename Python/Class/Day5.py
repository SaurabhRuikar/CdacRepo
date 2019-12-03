                     #LOCAL AND GLOBAL VARIABLES
'''
def f1():
    global x
    x=5
    print(x)

x=10
print(x)
f1()
print(x)
f1()
print(x)
'''
'''
#WITHOUT GLOBAL X

============ RESTART: /home/student/Desktop/Python/Class/Day5.py ============
10
5
10
5
10
>>> 

#WITH GLOBAL X

============ RESTART: /home/student/Desktop/Python/Class/Day5.py ============
10
5
5
5
5
'''

'''
def f1():
    x=15
    print(x)
    def f2():
        x=23
        print(x)
    f2()
    print(x)

x=10
print(x)
f1()
print(x)
'''

'''
#FUNCTION DEFINED INSIDE A FUNCTION NEEDS TO BE CALLED INSIDE THAT FUNCTION ITSELF.

def f1():
    x=15
    print(x)
    def f2():
        nonlocal x
        x=23
        print(x)
    f2()
    print(x)

x=10
print(x)
f1()
print(x)


def f1():
    x=15
    print(x)
    def f2():
        global x
        x=23
        print(x)
    f2()
    print(x)

x=10
print(x)
f1()
print(x)



#When x is global in f2
============ RESTART: /home/student/Desktop/Python/Class/Day5.py ============
10
15
23
15
23
>>> 
#when x is nonlocal in f2
============ RESTART: /home/student/Desktop/Python/Class/Day5.py ============
10
15
23
23
10
>>> 
'''


#File Handling

'''
cnt=1
fh=open("myfile.txt")
fh1=open("myfileop.txt","w")
for ln in fh:
    fh1.write(str(cnt)+":"+ln)
    print(str(cnt)+":"+ln,end="")
    cnt=cnt+1
fh.close()
fh1.close()
'''

'''
count=1
with open("myfile.txt") as fh:
    with open("file.txt","w") as fh1:
        for ln in fh:
            fh1.write(str(count)+" : "+ln)
            count += 1
'''






#Seek and Tell functions in File

fh=open("myfile.txt")
fstr=fh.read(5)
#print(fstr[3:10])
#print(fstr)
print(fh.tell())
fh.seek(0)
print(fh.tell())
























