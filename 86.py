s=input()
l=list(s)
c=0
for i in range(1,len(l)):
	if l[i]==l[i-1]:
		c=c+1
if c==0:
	print("Yes")
else:
	print("No")
