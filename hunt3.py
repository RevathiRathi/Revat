n=int(input())
l=[int(x) for x in input().split()]
a=[]
for i in range(0,len(l)):
	if l[i]==i:
		a.append(l[i])
if len(a)!=0:
	print(*a)
else:
	print(-1)
    
