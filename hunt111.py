#r
n=int(input())
l=[]
c=0
for i in range(n):
    l1=[int(x) for x in input().split()]
    l.append(l1)
for i in range(n):
    for j in range(n):
        if (i+j)==(n-1):
            c=c+l[i][j]
print(c)
