#rr
n,l,r=map(int,input().split())
l1=[int(x) for x in input().split()]
l1.sort()
for i in l1:
    if i>=l and i<=r:
        print(i)
        break
