#reva
s=input()
x=""
for i in s:
	if i not in x:
		x+=i
print(x[::-1])
