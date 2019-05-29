#r
s=input()
l=s.split(" ")
a=1
for i in range(len(l)):
    if l[i][0].isupper():
        a=1
    else:
        a=0
        break
if a==1:
    print("yes")
else:
    print("no")
