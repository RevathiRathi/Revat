#rrrrr
s=input()
li=[]
for i in s:
    if int(i)%2==1:
        li.append(i)
print(*li)
