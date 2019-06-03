#rrr
s=input()
a=""
c=0
l=[]
if s==s[::-1]:
    l.append(0)
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        a=s[i:j+1]
        if a==a[::-1]:
            l.append(len(s)-len(a))
print(min(l))
