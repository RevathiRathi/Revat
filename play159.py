#r
n,k=map(int,input().split())
r=n*k
s=bin(r)[2::]
print(s.count("1"))
