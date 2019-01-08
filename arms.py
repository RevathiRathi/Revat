n=int(input())
sum=0
temp=n
while n>0:
	s=n%10
	sum+=s**3
	n//=10
if temp==sum:
	print("yes")
else:
	print("no")
