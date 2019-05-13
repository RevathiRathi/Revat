n=int(input())
l=[int(x) for x in input().split()]
a=[]
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			if l[i] not in a:
				a.append(l[i])
			break
a.sort()
if len(a)==0:
	print("Unique")
else:
	for i in range(0,len(a)-1):
		print(a[i],end=" ")
	print(a[len(a)-1])
