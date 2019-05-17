#rev
n=int(input())
l=[int(x) for x in input().split()]
c=0
s=0
for i in range(0,len(l)):
	if l[i]%2==0:
		c+=1
		a=l[i]
	else:
		s+=1
		b=l[i]
if c==1:
	print(a)
else:
	print(b)
