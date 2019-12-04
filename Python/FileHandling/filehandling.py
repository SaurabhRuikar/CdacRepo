import sys
import os
from filefunctions import *


path='/home/student/Desktop/Python/FileHandling/SalaryModi.txt'


if os.path.exists(path):
    with open(path) as f:
        flst = f.readlines()
    
else:
    flst = []
count = len(flst)


wflag = False
dflag = False
ch = 0
while ch < 5:
    print('--------------------------')
    print('1. Read/Display data')
    print('2. Write data')
    print('3. Update data')
    print('4. Exit with saving')
    print('--------------------------')
    ch = int(input("Enter choice"))

    if ch == 1:
        read(flst)
        
    elif ch == 2:
        write(flst)
        wflag = True
        count += 1
        
    elif ch == 3:
        c = 0
        while c != 3:
            print('--------------------')
            print('1. Delete')
            print('2. Modify Salary')
            print('3. Exit')
            print('--------------------')
            c = int(input('Enter the choice : '))

            if c == 1:
                eid = int(input("Enter Employee ID for delete "))
                if delete(flst,eid):    
                    print('Deleted Sucessfully')
                    dflag = True
                else:
                    print('Not found!!')
            elif c == 2:
                eid = int(input("Enter Employee ID to modify : "))
                if modify(flst, eid):
                    print("Succefully Modified")
                    dflag = True
                else :
                    print("not modified")
    else :
        if dflag:
            with open(path, 'w') as fw:
                for i in flst:
                    fw.write(i)
            print('overwritten')
        elif wflag:
            with open(path, 'a') as fa:
                for i in flst[count-1:]:
                    fa.write(i)
            print('appended')
        else:
            print('not modified')
        sys.exit(0)    
