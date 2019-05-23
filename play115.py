#reva
n,k=map(str,input().split())
if len(n)==len(k):
	a=n
	b=k
else:
	if len(n)>len(k):
		a=n[:len(k)]
		b=k
	else:
		a=k[:len(n)]
		b=n
print(a+b)
