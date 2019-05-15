#revvv
g=int(input())
a=[]
for i in range(1,g+1):
	if g%i==0:
		if i%2==0:
			a.append(i)
print(*a)
