#reva
s,k=map(str,input().split())
k=int(k)
l=[]
for i in range(k-1,len(s),k):
    l.append(s[i])
print(*l)
