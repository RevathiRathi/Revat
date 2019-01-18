n=input()
a,d=0,0
for i in n:
	if i.isalpha():
		a=1
	elif i.isdigit():
		d=1
	if a==1 and d==1:
		print("Yes")
		break
if a==0 and d==0:
	print("No")
