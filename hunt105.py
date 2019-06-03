#r
n=int(input())
s=0
m=len(str(n))
while n>0:
    a=int(n)%10
    s=s+(a**m)
    n=n//10
print(s)
