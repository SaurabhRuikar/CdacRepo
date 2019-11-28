num=int(input("Enter the days in Month"))
n=int(input("Enter the start of the month"))

print("S","M","T","W","T","F","S",sep="\t")
spaces=n-1
i=1

print("\t"*spaces,end="")

i=1
while i<=num:
    print(i,end="\t")
    i+=1
    n=n+1
    if n==8:
        print()
        n=1




