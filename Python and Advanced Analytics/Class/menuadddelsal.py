choice=0
while choice!=4:
    print("1.To add new entry")
    print("2.To update salary of employee")
    print("3.For deleting employee from the file")
    print("4.Exit")

    choice=int(input("enter the choice"))
    if choice==1:
        fh=open("salary1.txt","a")
        eno=input("Enter the employee no")
        ename=input("Enter the employee name")
        dep=input("Enter the department")
        sal=input("Enter the salary")
        des=input("Enter the designation")
        s=[eno,ename,dep,sal,des]
        s1=":".join(s)
        print(s1)
        fh.write(s1)
        fh.close()
        
    elif choice==2:
          fh=open("salary1.txt")
          lst=fh.readlines()
          for i in lst:
              if i.split(":")
        
    elif choice==3:
        fh=open("salary1.txt")
        lst=fh.readlines()



        eno=input("Enter the employee no.you want to delete")
        for i in lst:
            if i.split(":")[0]==eno:
                lst.remove(i)
                print(lst)
        fh1=open("salary1.txt","w")
        fh1.writelines(lst)
        fh1.close()

















