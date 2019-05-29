#r
n=int(input())
for i in range(n,0,-1):
    s=[]
    for _ in range(i,0,-1):
        s.append("1")
    print(' '.join(s))
