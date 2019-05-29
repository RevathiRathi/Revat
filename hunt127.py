#r
s,a=map(str,input().split())
l=[]
if a in s:
    print(a)
else:
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if s[i]==a[j]:
                l.append(s[i])
print(''.join(l),end="")
