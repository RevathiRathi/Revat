#r
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
    if l[i]<=k:
        c+=1
print(c)
