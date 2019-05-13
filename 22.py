n,k=map(int,input().split(" "))
l=[]
for i in range(n,k+1):
	if n%i==0 and k%i==0:
		l.append(i)
print(*l)
