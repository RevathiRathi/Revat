#reva
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
a=""
for i in range(0,k):
	l.remove(l[-1])
for i in range(0,len(l)):
	a=a+str(l[i])+" "
print(a.strip())
