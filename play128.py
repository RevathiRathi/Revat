#reva
n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in l:
    c=c*i
if c%2==0:
    print("even")
else:
    print("odd")
