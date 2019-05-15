#rev
n=int(input())
l=list(map(int,input().split()))
r=0
for i in range(n):
	s=sum(l[i::2])
	if r<s:
		r=s
print(r)
