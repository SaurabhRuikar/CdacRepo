lst=[12,1,3,7,8,5,8]
print(lst)
lst1=[]
max=max(lst)
x = 0
while x<=max:
    lst1.append(-1)
    x += 1
print(lst1)

for i in lst:
    if lst1[i]!=-1:
        pos = lst.index(i)
        
    lst1[i] = lst.index(i)

print(lst1)
    
    
    
 
