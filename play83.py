#rev
n=int(input())
l=[int(x) for x in input().split()]
a=l[0]
for i in range(1,len(l)):
	a=a|l[i]
print(a)
