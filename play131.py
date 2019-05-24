#rr
n=input()
c=0
for i in range(0,len(n)):
    if int(n[i])%2==1:
        c=c+int(n[i])
if c%2==0:
    print("E")
else:
    print("O")
