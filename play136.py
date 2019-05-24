#rr
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in l:
    if i==k:
        print("yes",l.count(k))
        break
    else:
        print("no")
