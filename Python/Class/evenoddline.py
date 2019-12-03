'''
cnt=1
fh=open("myfile.txt")
fh1=open("even.txt","a")
fh2=open("odd.txt","a")
for ln in fh:
    if cnt%2==0:
        fh1.write(ln)
    else:
        fh2.write(ln)
    cnt=cnt+1    
fh.close()
fh1.close()
fh2.close()
'''

cnt=1
with open("myfile.txt") as fh:
    for ln in fh:
        with open("even3.txt","a") as fh1:
            if cnt%2==0:
                fh1.write(ln)
            else:
                with open("odd3.txt","a") as fh2:
                    fh2.write(ln)
            cnt=cnt+1
