#r
n,k=map(int,input().split())
l=[]
a=[]
for i in range(n):
    l1=[int(x) for x in input().split()]
    l.append(l1)
    if i in l:
        m=l.index(i)
        a.append(m)
for i in range(len(l)):
    if i in l[i]:
        for j in range(k):
            l[i][j]=0
for i in a:
    for j in range(n):
        l[i][j]=0
for i in l:
    print(*i)
