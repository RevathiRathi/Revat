#rev
n=int(input())
l=[int(x) for x in input().split()]
s=[0]
for i in range(n):
    for j in range(i,n):
        c=l[i:j+1]
        s.append(sum(c))
print(min(s))
