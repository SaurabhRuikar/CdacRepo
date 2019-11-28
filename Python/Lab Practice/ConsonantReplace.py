'''
Q. 1. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite colour
4. Sort and print students and their favourite colours alphabetically by name
Write a function translate() that will translate a text into "rövarspråket" (Swedish for
"robber's language").
That is, double every consonant and place an occurrence of "o" in between. For
example, translate("this
is fun") should return the string "tothohisosisosfofunon".



p={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("No of students - ")
print(len(p))


c=input("Enter the new color for Lisa ")
print("Previous color of Lisa")
print(p["Lisa"])

p["Lisa"]=c
print("New color for Lisa is ")
print(c)

print(p)
print()

p.pop("Jenny")
print(p)



for i in sorted(p):
    print(i,"---->",p[i])

'''

s=input("Enter the string")
print(s)
s1="aeiouAEIOU"
s2=""
for i in s:
        
        if i in s1:
            s2+=i
        else:
            s2+=i+"o"+i
print(s2)            
            
    



