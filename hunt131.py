#rr
n=int(input())
l=[int(x) for x in input().split()]
s=[]
l1=sorted(l)
while len(l1)!=0:
    if len(l1)!=1:
        s.append(l1[-1])
        s.append(l1[0])
        l1.remove(l1[0])
        l1.remove(l1[-1])
    else:
        s.append(l1[0])
        l1.remove(l1[0])
print(*s)	
