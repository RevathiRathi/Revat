#reva
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l1=list(set(l))
for i in range(0,len(l1)):
	if l.count(l1[i])==k:
		print(l1[i])
