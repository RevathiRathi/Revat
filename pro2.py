n,k=map(int,input().split(" "))
n=str(n)
l=[]
s=len(n)-k
for i in range(0,(len(n)-s)+1):
	d=n[i:i+s]
	l.append(d)
print(min(l))
