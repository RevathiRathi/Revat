n,k=map(int,input().split())
l=[]
for i in range(n+1,k+1):
	if i%2!=0:
		l.append(i)
for i in range(len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
