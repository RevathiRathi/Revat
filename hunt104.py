#r
n=input()
s=0
for i in range(0,len(n)):
    for j in range(0,i+1):
        s+=int(n[j])
print(s)
