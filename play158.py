n,k=map(int,input().split())
r=n*k
s=bin(r)[2::]
a=s[::-1]
b=a.index("1")
print(b+2)
