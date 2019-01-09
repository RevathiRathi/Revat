n=input()
c=0
for i in n:
	if i.isnumeric():
		c=c
	elif i.isalpha():
		c=c
	elif i.isspace():
		c=c
	else:
		c+=1
print(c)
	
