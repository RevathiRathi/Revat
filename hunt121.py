#r
s=input()
a=""
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)+1):
        b=s[i:j+1]
        if len(b)>len(a) and b==b[::-1]:
            a=b
print(a)
