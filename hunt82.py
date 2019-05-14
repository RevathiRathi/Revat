n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l=sorted(l)
for i in range(len(l)-1):
	print(l[i],end=" ")
print(l[len(l)-1])
