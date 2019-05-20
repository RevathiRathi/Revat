#reva
n,r=map(int,input().split())
s=0
for i in range(n,r+1):
	if i%2!=0:
		s=s+i
print(s)
