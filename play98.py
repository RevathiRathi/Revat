#reva
n,k=map(str,input().split())
k=int(k)
c=0
for i in range(k):
	if str(i) in n:
		c+=1
if c==k:
	print("yes")
else:
	print("no")
