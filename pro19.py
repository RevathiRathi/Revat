n=int(input())
a,b=[],[]
for i in range(0,n):
  a=sorted(list(map(int,input().split())))
  b=b+a
print(*sorted(b))
