#r
n,m=input().split(" ")
r=""
while n!="" and m!="":
	r+=n[0]+m[0]
	n=n[1:]
	m=m[1:]
a=1
if n!="":
	while n!="":
		r+=n[0]
		r+=str(a)
		n=n[1:]
		a+=1
else:
	while m!="":
		r+=str(a)
		r+=m[0]
		m=m[1:]
		a+=1
print(r)
