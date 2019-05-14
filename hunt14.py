from itertools import permutations
r=input()
p=permutations(r)
for i in list(p):
	print(''.join(i))
