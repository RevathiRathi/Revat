#rrrrr
s=input()
s1=input()
a=""
for i in range(len(s)):
    for j in range(len(s),-1,-1):
        if (s[i:j] in s1):
            if(len(s[i:j])>=len(a)):
                a=s[i:j]
print(a)
