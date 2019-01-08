n=int(input())
i=2
c=0
while i<=n-1:
	if n%i==0:
		c=c+1
		break
	i=i+1
if c!=0:
	print("no")
else:
	print("yes")
