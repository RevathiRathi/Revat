#rev
r,k=map(int,input().split())
while r>1:
    r=r/k
if r==1:
    print("yes")
else:
    print("no")
