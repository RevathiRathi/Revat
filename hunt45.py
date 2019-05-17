#reva
n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(1,n+1):
	if n*i in l:
		c+=1
print(c)
