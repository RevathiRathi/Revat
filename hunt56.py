#r
n=int(input())
l=[int(x) for x in input().split()]
a=1000
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if abs(l[i]+l[i+1])<a:
            a=abs(l[i]+l[i+1])
            r,g=l[i],l[i+1]
print(r,g)
