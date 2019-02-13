#reee
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	c=c+1
	if c==k:
		print(l[i])
