#reva
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
q=[]
for i in range(0,len(l)):
	if l[i]<k:
		q.append(l[i])
		q.sort()
print(*q)
