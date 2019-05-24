#reva
n=int(input())
l=[int(x) for x in input().split()]
for i in range(1,len(l)):
    if l[i]-l[i-1]==1:
        print("yes")
        break
    else:
        print("no")
        break
