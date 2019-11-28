s1=input("Enter the string")
print(s1)
s2=input("Enter the string to find")
print(s2)

cnt=0
pos=0
while pos!=-1:
    pos=s1.find(s2,pos)
    if pos==-1:
        break
    print(s2,"-",pos)
    cnt=cnt+1
    pos+=1

print(cnt)



