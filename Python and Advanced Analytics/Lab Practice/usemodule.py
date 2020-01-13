#import mymodule as m
import sys
from mymodule import *

choice=0
while choice!=4:
    print("1.Factorial")
    print("2.printtable")
    print("3.Prime")
    print("4.exit")

    choice=int(input("Enter the choice"))

    if choice==1:
        num=int(input("Enter the number"))
        f=factorial(num)
        print("factorial",f)

    elif choice==2:
         num=int(input("Enter the number"))
         printtable(num)
         printtable()

    elif choice==3:
        num=int(input("Enter the number"))
        prime(num)
        
    else:
        sys.exit(0)
    
