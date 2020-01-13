def read(flst):
    for i in flst:
      print(i,end="")
    print()

def write(flst):
    lst = []
    lst.append(input("Enter  ID "))
    lst.append(input("Enter  Name"))
    lst.append(input("Enter  Dept"))
    lst.append(input("Enter Salary "))
    lst.append(input("Enter Designation"))
    flst.append(":".join(lst))
    
def delete(flst, eid):
    ind = 0
    for i in flst:
        if eid == int(i.split(':')[0]):
           flst.pop(ind)
           return True
           break
        ind += 1
    else:
        return False

def modify(flst, eid):
    ind = 0
    for i in flst:
        if eid == int(i.split(':')[0]):
            data = i.split(':')
            print("previous salary ",int(data[3]))
            sal = input('Enter the new salary : ')
            data[3] = sal
            flst[ind] = ":".join(data)
            return True
            break
        ind += 1
    else:
        return False
