n=int(input())
l=list(map(int,input().split()))
m=max(l)
a,b=0,0
for i in range(0,len(l)-1):
  for j in range(i+1,len(l)):
    if abs(l[i]+l[j])<m:
      a,b=l[i],l[j]
      m=abs(a+b)
print(a,b)
