#r
n=input()
c=1
for i in range(len(n)-1):
    a=n[i]+n[i+1]
    b=int(a)
    if b<=26 and n[i]!="0":
        c+=1
if c==3:
    print(c)
else:
    print(c+(c-1)//2)
