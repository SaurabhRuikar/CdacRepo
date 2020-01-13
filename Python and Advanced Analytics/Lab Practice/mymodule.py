def factorial(n):
    print("name : ",__name__)    

    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

def printtable(n=5):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)


def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
            
        

if __name__=="__main__":
    f=factorial(4)
    print(f)
    printtable(3)
    printtable()
