n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
b=min(a)
for i in range(0,len(a)):
  for j in range(i,len(a)):
    for k in range(j,len(a)):
      val=p*a[i]+q*a[j]+r*a[k]
      if val>b:
        b=val
print(b)
