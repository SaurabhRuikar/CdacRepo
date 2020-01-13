s=input("Enter a string to be checked as palindrome")
s1=s[0:]
s1=s1.lower()

s2=s1.replace(" ","")
s2=s2.strip("'?!.")

if "'" in s2:
    s2=s2.replace("'","")
print(s2)
    


s3=s2[::-1]
print(s3)



if s3==s2:
    print("Is a Palindrome")
else:
    print("Not a palindrome")

