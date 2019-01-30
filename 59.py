n=int(input())
c=0
temp=n
while temp!=0:
	r=temp%10
	temp=temp//10
	c=c+1	
print(c)
