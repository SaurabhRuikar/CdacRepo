lst=[12,1,3,7,8,5,8]
nlst=[]
m=max(lst)
x=0
while x<=m:
    nlst.append(-1)
    x=x+1
print(nlst)
i=0

##while i<len(lst):
##    nlst[lst[i]]=i
##    i=i+1
##print(nlst)


i=0
for j in lst:
   nlst[j]=i
   i=i+1
print(nlst)   
