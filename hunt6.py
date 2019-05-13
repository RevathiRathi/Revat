n=int(input())
l=[int(x) for x in input().split()]
a=[]
c=0
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			a.append(l[i])
			c=c+1
print(a[0])
if c==0:
	print("unique")
