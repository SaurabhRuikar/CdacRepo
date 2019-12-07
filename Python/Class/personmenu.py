from personclass import *
from SalException import SalaryException

def addPerson(lst):
    pid=int(input("Enter the pid"))
    name=input("Enter the name")
    mob=input("Enter the mobile no")
    p=Person(pid,name,mob)
    lst.append(p)

def DisplayData(lst):
    for p in lst:
        print(p)
        print("-----------------------")

def deletePerson(lst,pid):
    pos=searchById(lst,pid)
    if pos!= -1:
        print(lst[pos])
        ans=input("Delete yes or no y/n")
        if ans=="y":
            lst.pop(pos)
            return True
        else:
            return False
        

    
    
def searchById(lst,pid):

    count=0
    for i in lst:
        if i.getPid()==pid:
            return count

        count=count + 1

    else:
        return -1

def modifyPersonMob(lst,pid,mob):
    pos=searchById(lst,pid)

    if pos!= -1:

        lst[pos].setMob(mob)
        return True
    else:
        return False

def searchByName(lst,name):
    
    count=0
    for i in lst:
        if i.getName()==name:
            return count

        count=count + 1

    else:
        return -1



def addSalaried(lst):
    
    pid=int(input("Enter the pid"))
    name=input("Enter the name")
    mob=input("Enter the mobile no")
    dept=input("Enter the department")
    desg=input("Enter the designation")
    for i in range(3):
        try:
            sal=int(input("Enter the salary"))
            if sal<1000:
                raise SalaryException("Salary should be greater then or equal to 1000")
            bonus=int(input("Enter the bonus"))
            s=SalariedEmp(pid,name,mob,dept,desg,sal,bonus)
            lst.append(s)
            break
        except SalaryException as e:
            print(e)
    else:
        print("Wrong Input thrice! chances over")
 




def addContract(lst):
    pid=int(input("Enter the pid"))
    name=input("Enter the name")
    mob=input("Enter the mobile no")
    dept=input("Enter the department")
    desg=input("Enter the designation")
    hrcharges=int(input("Charges per hours"))
    nohrs=int(input("Enter the no.of hours"))
    c=Contract(pid,name,mob,dept,desg,hrcharges,nohrs)
    lst.append(c)


    
                    
    
