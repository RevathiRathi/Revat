import math
n,m=map(int,input().split(" "))
pro=n*m
n=math.sqrt(pro)
m=math.floor(n)
if n==m:
	print("yes")
else:
	print("no")
