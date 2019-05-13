n,k=map(int,input().split(" "))
c=0
for i in range(n,k+1):
	for j in range(1,i+1):
		if j**2==i:
			c+=1
print(c)
