'''
print("Hello World")

a = 10 

print (type(a),a)

a = "Ankit"

print (type(a),a)


b=input("Enter no.")

print("You have entered",b)

print("You have entered"+b)


c = int(input("Enter number "))
if c==12:
	print("value of c is 12")
else:
	print("value of c is not 12")
'''

#this is a single line comment in Python

'''
d= int(input("Enter number "))
e= int(input("Enter number "))
f= int(input("Enter number "))
if d>e:
	if d>f:
		print("d is greater",d)
	else:
		print("f is greater",f)
else:
	if e>f:
		print("e is greater",e)
	else:
		print("f is greater",f)
'''

#While Demo
'''
i=0
while i<=10:
	#print(i)
	print("helu")
	i=i+1




#Program to Display the table of a entered number

x=int(input("Enter a number"))
i=1
while i<=10:
	a = x * i
	print(x,"*",i,"=",a)
	i=i+1




	
a ="s"*5
print(a)


#Printing Multiple lines on same line using seperate print statements.By def end parameter in print is set to \n so it pushes always to new line. Here we replace it with a blank space.
print("Hello",end=" ")
print("World")


#Prints 3 string with a | seperator here. by def the sep paramater is set to have an space. Here we replace it with a | symbol
print("asdsad","adsada","asdsadwer",sep="|")

print("asdsad","adsada","asdsadwer",sep="***")
'''



'''

java = int(input("Enter marks for java "))
maths = input("Enter marks for maths ")
geo = input("Enter marks for geography ")


print("You ward has secured",java,"marks in java",maths,"marks in maths",geo,"marks in geography")

	#alternate way

print("You ward has secured "+str(java)+" marks in java")

	#alternate way

print("your ward secured %5d in Java and %s in maths" %(java,maths))
	
	# %5d will reserve it for having only 5 digits and if your input fewer than 5 they remain empty
	#alternate way

print("your ward secured {0} in java and {1} in maths".format(java,maths))

'''



















