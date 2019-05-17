#rev
n=int(input())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
p=[]
for i in l:
	if i in l1:
		p.append(i)
k=set(p)
k=sorted(k)
print(*k)
