import sys
import personclass as p
from personclass import Person
from personmenu import*
##q=Person(113,"Saurabh","64634389843")
##p=p.Person(112,"Ankit","6461144121")
##print(p)
##print(q)
##
## 

plist=[]
choice=0
while choice !=9:
    print("1. Add New Person")
    print("2. Delete Person")
    print("3. Modify Person")
    print("4. Display by Id")
    print("5. Display All")
    print("6. Display by Name")
    print("7. Employee Type")
    print("8. Salary Calculation")
    print("9. Exit")
    choice = int(input("Enter you choice: "))

    if choice==1:
        addPerson(plist)
        

    elif choice==2:
        pid=int(input("Enter pid for deleting Person"))
        ans=deletePerson(plist,pid)
        if ans==True:
            print("Deleted Successfully")
        else:
            print("Not Found")
        
    elif choice==3:

        pid=int(input("Enter pid for Search"))
        mob=input("Enter mobile for modification")
        ans=modifyPersonMob(plist,pid,mob)
        if ans==True:
            print("Updated Successfully")
        else:
            print("Not Found")
    
            
    elif choice==4:
        
        pid=int(input("Enter pid for search"))
        pos=searchById(plist,pid)
        if pos!= -1:
            print(plist[pos])
        else:
            print("Id not Found")
    
    elif choice==5:
        DisplayData(plist)

    elif choice==6:

        name=input("Enter name for search")
        pos=searchByName(plist,name)
        if pos!= -1:
            print(plist[pos])
        else:
            print("Name not Found")


    elif choice==7:
        emp=input("Do you want to add salaried Employee or Contract Employee  s/c")

        if emp=="s":
            addSalaried(plist)

        else:
            addContract(plist)
           
           
    elif choice==8:
        pid=int(input("Enter Pid to be used for Salary Calculation : "))
        
        pos=searchById(plist,pid)
        if pos!= -1:
           #if isinstance(plist[pos],SalariedEmp):
            print(plist[pos].calcSal())

           # else:
           #    print(plist[pos].calcSal())
                
            

        else:
            print("Id not Found")
           
       
        
    else:
        sys.exit(0)
