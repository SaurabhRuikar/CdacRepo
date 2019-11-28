di={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t','h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T','H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F',
'T':'G', 'U':'H', 'V':'I','W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

s=input("Enter a string ")
s1=input("Do you want to encode or decode the string? e/d")



if s1=="e":
    s2=list(s)
    for i in s2:
        for n in di.keys():
            if n==i:
                print(di[n], sep=" ",end=" ")
    print()
    print("Encoded Successfully!")

'''       
else:
     s2=list(s)
     for i in s2:
        for n in di.keys():
            if n==i:
                print(di[n], sep=" ",end=" ")
     print()
     print("Decoded Successfully!")
'''
