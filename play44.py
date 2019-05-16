s,k=map(str,input().split())
k=int(k)
c=len(s)
a=s
for i in range(0,k):
	a=a[-1]+a[:c-1]
print(a)
