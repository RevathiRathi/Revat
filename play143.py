#rr
n=int(input())
l=[int(x) for x in input().split()]
w=[int(c) for c in input().split()]
s=sorted(w)
b=[]
for i in s:
    a=w.index(i)
    b.append(l[a])
print(*b)
