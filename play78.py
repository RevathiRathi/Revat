#rev
n=map(int,input().split())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
l2=l+l1
print(*sorted(l2))
