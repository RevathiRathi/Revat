#rr
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
m=0
if k in l:
    print(k)
else:
    for i in l:
        if i>m and i<k:
            m=i
    print(m)
