#r
n=input()
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
	if i%2==0:
		if l[i]%2!=0:
			k.append(l[i])
	else:
		if l[i]%2==0:
			k.append(l[i])
for i in k:
	print(i,end=" ")
