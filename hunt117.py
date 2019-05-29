#r
n=int(input())
s=str(n)
c=0
for i in range(0,len(s)):
    c=c+int(s[i])**i
print(c)
