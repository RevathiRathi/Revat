n=input()
t=input().split()
c=0
s=input()
for i in t:
	if s==i[:len(s)]:
		c+=1
print(c)
