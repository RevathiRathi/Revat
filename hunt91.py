#rr
from itertools import permutations
s=input()
c=0
a=permutations(s)
for i in a:
    if all(i[j]!=i[j-1] for j in range(1,len(i))):
        c+=1
        break
    else:
        c=0
if c>0:
    print("yes")
else:
    print("no")
