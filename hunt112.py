#r
s=input()
x=input()
l=""
if len(s)>=len(x):
    for i in range(0,len(s)):
        for j in range(0,len(x)):
            if s[i]==x[j] and i>=j and x[j] not in l:
                l=l+x[j]
else:
    for i in range(0,len(s)):
        for j in range(0,len(x)):
            if s[i]==x[j] and i<=j and x[j] not in l:
                l=l+x[j]
print(l)
