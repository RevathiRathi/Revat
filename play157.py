#rr
n,k=map(int,input().split())
r=n*k
s=bin(r)[2::]
a=s[::-1]
c=a.index("1")
print(c+1)
