#r
n=input()
s=[]
for i in range(0,len(n)-1):
    if n[i]==n[i+1]:
        d=n[:i+1]+n[i+2:]
        s.append(d)
s.sort()
print(s[-1])
