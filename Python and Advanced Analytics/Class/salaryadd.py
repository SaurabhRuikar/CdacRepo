sal=0
fh=open("salary.txt")
for ln in fh:
    sal=sal+float(ln.split(":")[3])
print("addition is",sal)    
    
    
    
