##lst=["xyz","ayz","pqr","ayz"]
lst=[]

ans="y"
while ans=="y":
    s=input("Enter the string")

    for i in lst:
        if s[1]==i[1]:
            lst.insert((lst.index(i)),s)
            print(lst)
            break
        
    else:
        lst.append(s)
    ans=input("do you want to add more string y/n")
            
print(lst)
        
##        print("Not matching")
        
        

























    
##for i in lst:
##    if s[1]==i[1]:
##        lst.insert((lst.index(i)+1),s)
##    print(lst)
    
