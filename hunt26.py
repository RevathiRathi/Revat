n=int(input())
l=[int(x) for x in input().split()]
l1=l[::-1]
g=" "
for i in range(0,len(l1)):
	g=g+str(l1[i])+"->"
print(g[:len(g)-2])
