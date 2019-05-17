#rev
n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		if l[i]<l[j]:
			print(l[j],end=" ")
			break
		else:
			print(l[i],end=" ")
			break
