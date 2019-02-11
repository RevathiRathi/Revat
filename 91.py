l,b,h=map(int,input().split())
vol=l*b*h
area=(l*b)+(b*h)+(h*l)
s=2*area
print(s,end=" ")
print(area)
