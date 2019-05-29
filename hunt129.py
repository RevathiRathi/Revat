#r
n=int(input())
l=[int(x) for x in input().split()]
l1=[]
for i in l:
    l1.append(l.count(i))
m=max(l1)
for i in range(0,len(l)):
    if l1[i]==m:
        print(l[i])
        break
