import sys

choice=0
while choice !=6:
    print("1. Display all empno and names")
    print("2. Display all emps earning greater than entered salary")
    print("3. Department wise Salary")
    print("4. Designation wise Salary")
    print("5. Designation wise Average Salary")
    print("6. Exit")

    choice=int(input("Enter your choice :"))
    if choice==1:

        fh=open("salary.txt")
        print("empno ename")
        for ln in fh:
            x=ln.split(":")[0]
            y=ln.split(":")[1]
            print(x, end=" ")
            print(y)
        
    elif choice==2:
        num=int(input("Enter number for which you want greater salary employees "))        
        fh=open("salary.txt")
        print("empno salary")
        for ln in fh:
            x=ln.split(":")[0]
            y=int(ln.split(":")[3])
            if y > num:
                print(x,y)
                break
        else:
            print("None of them have salary greater than",num)
            
    elif choice==3:
        di={}
        sal=0
        fh=open("salary.txt")
        for ln in fh:
            j=ln.split(":")[2]
            k=int(ln.split(":")[3])
            if j in di:
                sal=di[j]+k
                di[j]=sal
            else:
                di[j]=k
        
        for l in di.keys():
            print(l,"----->",di[l])
            

                
        
    elif choice==4:
        di={}
        sal=0
        fh=open("salary.txt")
        for ln in fh:
            j=ln.split(":")[4]
            r=j.rstrip()
            k=int(ln.split(":")[3])
            if r in di:
                sal=di[j]+k
                di[j]=sal
            else:
                di[j]=k
        for l in di.keys():
            print(l,end="")
            print(di[l])
            print()
                   
            
        



        
    elif choice==5:
        di={}
        fh=open("salary.txt")
        for ln in fh:
            data=ln.split(":")
            j = data[4].rstrip('\n')
            if j in di:
                di[j][0] += int(data[3])
                di[j][1] += 1
            else:
                di[j] = [int(data[3]), 1]

        for i in di.keys():
            di[i] = di[i][0]/di[i][1]
        print(di)
            
        
    else:
        sys.exit(0)
