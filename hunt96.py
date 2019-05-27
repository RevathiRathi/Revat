#rr
n=int(input())
if n<10:
    print(n)
else:
    a=n%9
    if a==0:
        print("9"*int(n/9))
    else:
        s=str(a)
        print(s,"9"*int(n/9),sep="")
