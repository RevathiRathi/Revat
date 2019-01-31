n=input()
c=0
for i in range(0,len(n)):
	if (n[i]=="a")or(n[i]=="e")or(n[i]=="i")or(n[i]=="o")or(n[i]=="u"):
		c=c+1
		break
if c!=0:
	print("yes")
else:
	print("no")
