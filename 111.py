n,k=map(int,input().split())
c=0
for i in range(n,k):
	i1=2
	while i1<n:
		if n%i1==0:
			break
		i1+=1
	if n==i1:
		c+=1
print(c)
