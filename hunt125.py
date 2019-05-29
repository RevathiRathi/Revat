#r
s=input()
l=[]
for i in s:
    if s.count(i)==1:
        l.append(i)
for i in range(0,len(l)-1):
    print(l[i],end="")
print(l[-1])
