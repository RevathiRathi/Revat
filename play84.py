#rev
n=int(input())
l=[int(x) for x in input().split()]
s=[]
if len(l)!=1:
	for i in range(n-1):
		s.append(l[i]|l[i+1])
else:
	s.append(l[0])
print(max(s))
