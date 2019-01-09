n=int(input())
l=[int(x) for x in input().split()]
l.sort()
for i in range(len(l)-1):
	print(l[i],end=" ")
print(l[-1])
