#reva
n=int(input())
l=[int(x) for x in input().split()]
s=max(l)
c=0
r=[]
for i in range(s,1000):
	c=0
	for j in range(0,len(l)):
		if i%l[j]==0:
			c+=1
	if c==len(l):
		r.append(i)
g=min(r)
print(g)			
