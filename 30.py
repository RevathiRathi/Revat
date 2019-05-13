n,s,k=map(str,input().split(" "))
k=int(k)
c=0
for i in range(len(n)):
	if n[i]!=s[i]:
		c+=1
if c==k:
	print("yes")
else:
	print("no")
