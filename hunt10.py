n,k=map(int,input().split(" "))
a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
c=0
for i in range(0,len(b)):
	if b[i] in a:
		c+=1
if len(b)==c:
	print("YES")
else:
	print("NO")
