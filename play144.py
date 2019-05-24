#rr
n=int(input())
l=[int(x) for x in input().split()]
a=[]
for i in range(0,len(l)):
    if l[i]%l[i-1]==0:
        a.append(l[i])
print(*a)
