#reva
n=int(input())
l=[int(x) for x in input().split()]
l1=0
for i in range(0,len(l)-1):
	sum=l[i]+l[i+1]
	l1=l1+sum
print(l1)
