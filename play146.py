#rev
a,b=map(int,input().split())
r=1
g=1
for i in range(1,a+1):
    r=r*i
for i in range(1,b+1):
    g=g*i
print(r//g)
