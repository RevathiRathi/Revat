#reva
n=int(input())
l=[int(x) for x in input().split()]
s=max(l)
c=0
r=[]
for i in range(1,s+1):
	c=0
	for j in range(0,len(l)):
		if l[j]%i==0:
			c+=1
	if c==len(l):
		r.append(i)
g=max(r)
print(g)			
