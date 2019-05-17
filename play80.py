#rev
n=map(int,input().split())
l=[int(x) for x in input().split()]
b=[]
for i in range(0,len(l)):
	for j in range(1,len(l)):
		if l[i]-l[j]!=0:
			b.append(abs(l[i]-l[j]))
print(min(b))
