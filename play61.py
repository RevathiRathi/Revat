#reva
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			print("yes")
			exit(0)
print("no")
