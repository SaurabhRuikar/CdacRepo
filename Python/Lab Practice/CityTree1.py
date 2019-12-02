'''
Write a program to display following menu
1. add new city and trees commonly found in city
2. Display all cities and the list of trees for all cities
3. display list of a particular city
Accept a city from user search city and if found display list of trees otherwise
display message not found
4. display cities containing tree
Accept a tree name from user and display all cities in which the tree is there
5. delete city - Accept city from user and delete the city if found
prompt user before deletion
6. modify tree listaccept city and trees to be added in the city. if city exist add trees at the end of the list
Otherwise add city and list
7. exit
'''

import sys
def add(city, cname):

    ans1="y"
    while ans1=="y":
        lst=[]
        ans="y"
        while ans=="y":
            tree=input("Enter the trees names ")
            lst.append(tree)
            ans=input("Do you want to add more trees y/n ")
        city[cname]=lst
        ans1=input("Do you want to add another city? y/n ")
    print(city)

def find(city):

    ans="y"
    while ans=="y":

        cname=input("Enter the city name")
        if city.get(cname,1)!=1:
            print(cname,"----->",city[cname])
        else:
            ("City not found")

        ans=input("Do you want to display trees for another City? y/n ")
                
def findSpecific(city):

    ans="y"
    while ans=="y":
        
        tree=input("Enter Tree for which you want to find a City ")
        print("Cities containing tree which you entered are:")

        for k,v in city.items():
            if tree in v:
                print(k)
            else:
                print("Tree not found")
            #print(k,"--->",v)
        ans=input("Do you want to search a tree again? y/n")


def delete(city):
    ans="y"
    while ans=="y":
        cname=input("Enter city that you want to delete? ")
        if city.get(cname,1)!=1:

              x=input("Do you want to delete this city? y/n ")
              if x=="y":
                  city.pop(cname)
                  print(city)
              else:
                  print("Not Deleted")
                  print(city)
                  
        else:
              print("Sorry, City not Found!")
              
        ans=input("Do you want to delete another city? y/n ")

def modify(city):
    ans5="y"
    while ans5=="y":
        cname=input("Enter the city name")
        if city.get(cname,1)!=1:
            ans3="y"
            while ans3=="y":
                tree=input("Enter the trees you want to add ")
                city[cname].append(tree)
                ans3=input("Do you want to add more trees? y/n")
            print(city)

        else:
            '''
            ans1="y"
            while ans1=="y":
                lst=[]
                print("City not found so add new city")
                cname=input("Enter the  new city name ")
                ans="y"
                while ans=="y":
                    tree=input("Enter the trees names ")
                    lst.append(tree)
                    ans=input("Do you want to add more trees y/n ")
                city[cname]=lst
                ans1=input("Do you want to add another city? y/n ")
            print(city)
            
            ans2=input("Do you want to modify another city? y/n")
            '''
            
            print("City not found so adding city in the dictionary") 
            add(city, cname)
        ans5=input("Do you want to continue? y/n ")
        



city={}

choice=0

while choice!=7:
    print("1. Add New City with Trees")
    print("2. Diplay all Cities and List of Trees")
    print("3. Display list of particular City")
    print("4. Display Cities containing Specific Tree")
    print("5. Delete City")
    print("6. Modify Tree List")
    print("7. Exit")

    choice=int(input("Enter a Choice "))

    if choice==1:
        cname=input("Enter the city name ")
        add(city,cname)
        
    elif choice==2:
        print(city)
        
    elif choice==3:
        find(city)
        
    elif choice==4:
        findSpecific(city)
    elif choice==5:
        delete(city)
    elif choice==6:
        modify(city)
    else:
          sys.exit(0)
