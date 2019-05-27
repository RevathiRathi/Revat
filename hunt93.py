#rr
s=input()
a=""
c=0
for i in range(len(s)):
    if s[i]==" ":
        a=a+s[i]
    elif c%2!=0:
        a=a+s[i]
        c+=1
    else:
        a=a+s[i].upper()
        c+=1
print(a)
