#r
n=int(input())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
i=l.index(l[n-2])
j=l1.index(l[i])
print(i-j)
