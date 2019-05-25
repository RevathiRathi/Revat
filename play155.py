#rr
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
a=l[:k]
b=l[k:]
a.sort()
b.sort(reverse=True)
print(*a,*b)
