n=int(input())
a=0
b=1
l=[]
for x in range(0,n):
	c=a+b
	a=b
	b=c
	l.append(a)
for a in range(len(l)-1):
	print(l[a],end=" ")
print(l[-1])
