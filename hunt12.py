n,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
d=1
while d<k:
	f=max(l)
	l.remove(f)
	d+=1
print(max(l))
