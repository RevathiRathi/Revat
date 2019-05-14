n=int(input())
l=[int(x) for x in input().split()]
l1=l[::-1]
a=" "
for i in range(0,len(l1)):
	a=a+str(l1[i])+"->"
print(a[:len(a)-2])
