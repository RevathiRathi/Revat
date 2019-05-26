#rr
n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
    l.append(input())
a=["a","e","i","o","u"]
for i in l:
    if any(j in i for j in a):
        c+=1
if c>=k:
    print("yes")
else:
    print("no")
