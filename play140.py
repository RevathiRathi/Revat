#rr
s=input()
if all(i=="a" or i=="b" for i in s):
    print("yes")
elif all(i=="a" for i in s):
    print("yes")
elif all(i=="b" for i in s):
    print("yes")
else:
    print("no")
