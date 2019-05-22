#reva
n=int(input())
a=[]
k=bin(2**n-1)[2::]
l=len(k)
for i in range(0,2**n):
	s=bin(i)[2::]
	if len(s)<l:
		a.append([s.count("1"),(l-len(s))*"0"+s])
		print(a)
	else:
		a.append([s.count("1"),s])
print(a)
