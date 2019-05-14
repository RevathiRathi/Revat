from itertools import combinations
n,k=map(int,input().split())
r=len(str(n))
l=list(combinations(str(n),r-k))
l=sorted(l)
print("".join(l[0]))
