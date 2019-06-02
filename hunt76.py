#r
n=int(input())
l=[]
for i in range(n):
    l1=[int(x) for x in input().split()]
    l.append(l1)
s=0
for i in range(n):
    s+=sum(l[i])
s=s/(n*n)
print("%.6f" %s)
