#reva
n,k=map(int,input().split())
p=[]
s=""
l1=list(map(int,input().split()))
for i in range(0,k):
	l1.append(l1[0])
	l1.remove(l1[0])
for i in l1:
   
        s=s+str(i)+" "
print(s.strip())
