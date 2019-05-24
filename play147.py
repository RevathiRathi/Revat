#rr
s=list(map(str,input().split()))
for i in range(1,len(s)):
    if i!=len(s)-1:
        s[i]=s[i][::-1]
print(*s)
