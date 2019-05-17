#rev
n=int(input())
l=[int(x) for x in input().split()]
a=l[0]
for i in range(0,len(l)):
	b=a|l[i]
print(b)
