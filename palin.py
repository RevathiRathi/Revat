N=v=int(input())
rev=0
rem=0
while N!=0:
    rem=N%10
    rev=(rev*10)+rem
    N=N//10
if v==rev:
	print("yes")
else:
	print("no")
