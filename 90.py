s=input()
s1=list(s)
for i in range(0,len(s1)):
	if s1[i].isnumeric():
		print(s1[i],end="")
