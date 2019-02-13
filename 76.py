#revs
s=input()
l=list(s)
for i in range(0,len(l)):
    if i==int(len(l)/2):
        l[i]="*"
        if len(l)%2==0:
            l[i-1]="*"
print("".join(l))
