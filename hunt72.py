s=input().split()
a=[]
for i in range(0,len(s)):
        if(i==(len(s)-1)):
                if((s[i][-1])=='.'):
                        s[i]=(s[i][:-1])
        if(i%2==0):
            b=s[i][::-1]
            a.append(b)
        else:
            a.append(s[i])
print(" ".join(str(x) for x in a)) 
