n,k=map(int,input().split(" "))
l=[]
for n in range(n+1,k):
    sum=0
    temp=n
    while n>0:
        s=n%10
        sum+=s**3
        n//=10
    if temp==sum:
        l.append(sum)        
for i in range(len(l)-1):
    print(l[i],end=" ")
print(l[-1])
