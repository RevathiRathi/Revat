#reva
n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
	if n*l[i]==n:
		c+=1
print(c)
