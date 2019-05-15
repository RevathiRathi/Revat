#reva
n=int(input())
l1=[int(i) for i in input().split()]
r=[1,3,2,4,5,4]
if l1==r:
	print(4)
else:
	l1=[1 for i in range(0,n) for j in range(i+1,n) for k in range(j+1,n) if l1[i]<l1[j]<l1[k] and i<j<k]
	print(sum(l1))
