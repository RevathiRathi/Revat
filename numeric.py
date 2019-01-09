n=input()
l=list(n)
f=1
for i in range(0,len(l)):
	if l[i].isdigit():
		pass
	else:
		f=0
		break
if f==1:
	print("yes")
else:
	print("No")
