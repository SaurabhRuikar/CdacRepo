num=int(input("Enter the days in Month"))
n=int(input("Enter the start of the month"))

print("S","M","T","W","T","F","S",sep="\t")
print("\t"*(n-2),end="\t")

i=1
while i<=num:
    print(i,end="\t")
    i+=1
    n+=1
    if n==8:
        print()
        n=1




        
##    elif n==1:
##        print(" ",i,end=" ")
##        i=i+1
##    
