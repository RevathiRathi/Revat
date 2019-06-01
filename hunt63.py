#r
n=int(input())
l=[int(x) for x in input().split()]
l1=[]
for i in range(len(l)-1):
    l2=l[i+1::]
    m=max(l2)
    l1.append(m)
l1.append(0)
print(*l2)
