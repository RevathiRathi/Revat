n=int(input())
s=list(map(str,input().split()))
p=sorted(s,key=len)
for i in range(len(p)-1):
    if len(p[i])==len(p[i+1]) and p[i]>p[i+1]:
        p[i],p[i+1]=p[i+1],p[i]
print(*p)
