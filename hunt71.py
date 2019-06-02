#r
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
a=[]
i=n-1
while k>0:
    a.append(l[i])
    k-=1
    i-=1
print(*a[::-1])
