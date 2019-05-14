import re
t=input()
r=re.sub(' +', ' ',t)
print(r.strip())
