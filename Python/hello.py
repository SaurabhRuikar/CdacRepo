
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
			
