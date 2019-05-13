n=int(input())
l=[str(x) for x in input().split()]
l.sort()
print("".join(l[::-1]))
