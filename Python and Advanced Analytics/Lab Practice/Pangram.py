s=input("Enter a string to be checked ")

s1=s.lower()

lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


l=len(lst)

print(len(s))
cnt=0

for i in lst:
    #print(i)
    if i in s:
        #print(i)
        cnt=cnt+1
        print(cnt)

if cnt<26:
    print("Not Pangram")
else:
    print("Pangram")


    
        
    
