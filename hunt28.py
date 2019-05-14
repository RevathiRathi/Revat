n=input()
s=list(n)
a=[]
b=""
for i in range(0,len(s)):
	if s[i] not in a:
		a.append(s[i])
print(b.join(a))
