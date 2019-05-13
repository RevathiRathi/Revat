s=input()
l=' '
for i in range(0,len(s)):
	if s[i].islower():
		l=l+s[i].upper()
	else:
		l=l+s[i].lower()
print(l)
