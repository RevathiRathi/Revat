#reva
s=input()
g=[]
r=[]
for i in s:
  if i=='(':
    g.append(i)
  elif i==')':
    r.append(i)
if len(g)==len(r):
  print("yes")
else:
  print("no")
