#r
s=input()
l=[]
for i in range(0,len(s)):
    for j in range(i+2,len(s)+1):
        a=s[i:j]
        if a==a[::-1]:
            l.append(a)
l.sort()
for i in range(0,len(l)):
    print(l[i])
