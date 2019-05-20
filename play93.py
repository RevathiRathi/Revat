#rev
n=int(input())
l=[int(x) for x in input().split()]
a=[]
for i in range(0,(n-1),2):
	l[i],l[i+1]=l[i+1],l[i]
	a.append(l[i])
	a.append(l[i+1])
if len(l)%2==1:
	a.append(l[-1])
print(*a)
