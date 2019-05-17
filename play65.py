#reva
n=int(input())
l=[int(x) for x in input().split()]
q=[]
for i in range(0,len(l)):
	if l[i]<n:
		q.append(l[i])
		q.sort()
print(*q)
