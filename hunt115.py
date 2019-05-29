#r
n=int(input())
l=[]
c=0
for i in range(1,n):
    d=0
    for j in range(1,i):
        if i%j==0:
            d+=1
    if d==1:
        l.append(i)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==n and l[i]<=l[j]:
            c+=1
print(c)
