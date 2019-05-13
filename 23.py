n,k=map(int,input().split(" "))
n=list(map(int,input().split(" ")))
k=list(map(int,input().split(" ")))
d=[]
for i in k:
	n.append(i)
	d.append(max(n))
print(*d)
