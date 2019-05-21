#reva
n,m=map(int,input().split())
l=[int(x) for x in input().split()]
a=l[0:n]
b=l[n:]
c=[]
for i in a:
	if i in b:
		c.append(i)
		b.remove(i)
print(*c)
