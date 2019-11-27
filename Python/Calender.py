num=int(input("Enter the days in Month"))
n=int(input("Enter the start of the month"))

print("S","M","T","W","T","F","S",sep="\t")

i=1

if n==1:
    while i<=num:
        print(i,end="\t")
        i+=1
        n=n+1
        if n==8:
            print()
            n=1
else:
    
    print("\t"*(n-2),end="\t")

    i=1
    while i<=num:
        print(i,end="\t")
        i+=1
        n=n+1
        if n==8:
            print()
            n=1




