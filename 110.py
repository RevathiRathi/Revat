s,n=map(str,input().split())
c=0
for i in range(0,len(s)):
	if s[i]!=n[i]:
		c=c+1
if c>1:
	print("yes")
else:
	print("no")
