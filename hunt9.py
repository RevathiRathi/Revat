n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if abs(l[i]+l[j])<=0:
			print(l[i],l[j])
		break
