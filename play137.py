#rr
n=int(input())
s=bin(n)[2::]
a=s[::-1]
print(a.index("1")+1)
