'''
#Write a program to accept names
# from users and store it in sets
#display following menu
print("""1. delete element if exists otherwise
do not show any errr""")
print("2. add a elemet")
print("3. create one more set")
print("4. union of 2 sets")
print("4. intersection of 2 sets")
print("5. difference of 2 sets")
print("6. convert set into frozenset")
print("6. exit")

'''


import sys
s=set()

ss="y"
while ss=="y":

    sr=input("Enter a name to be added")
    s.add(sr)
    ss=input("Do you want to continue? y/n")
    
print(s)
choice=0
while choice !=8:
    
    print("1. delete element")
    print("2. add more  elements")
    print("3. create one more set")
    print("4. union of 2 sets")
    print("5. intersection of 2 sets")
    print("6. difference of 2 sets")
    print("7. convert set into frozenset")
    print("8. exit")

    choice=int(input("Enter your choice of set operation "))

    if choice==1:

        ans="y"
        while ans=="y":
            x=input("Enter element to be deleted")
            s.discard(x)
            ans=input("Do you want to delete more elements? y/n")
        print(s)

    elif choice==2:

        ss="y"
        while ss=="y":
            sr=input("Enter a name to be added")
            s.add(sr)
            ss=input("Do you want to continue? y/n")
    
        print(s)

    elif choice==3:
        flag=0
        s9=set()

        ss="y"
        while ss=="y":
            sr=input("Enter a name to be added")
            s9.add(sr)
            ss=input("Do you want to continue? y/n")

        print("Newly Created set is : ")
        print(s9)
        print("Previously Created set is : ")
        print(s)
        flag=1
        
    
    elif choice==4:
        if flag==1:
            s10=s.union(s9)
            print(s10)
        else:
            print("First create another set and then choose this option again please. ")

    elif choice==5:
         if flag==1:
            s10=s.intersection(s9)
            print(s10)
         else:
            print("First create another set and then choose this option again please. ")

    elif choice==6:
         if flag==1:
            s10=s.difference(s9)
            print(s10)
         else:
            print("First create another set and then choose this option again please. ")

    elif choice==7:
        print("Previous")
        print(s)
        print("Newly created")
        print(s9)
        ans="y"
        while ans=="y":
            v=input("Convert newly created or previous set into frozen set? new/old")
            if v == "old":
                fs=frozenset(s)
                print(fs)
            else:
                fs=frozenset(s9)
                print(fs)        

            ans=input("Do you want to convert any more sets? y/n ") 
    else:   
        sys.exit(0)


