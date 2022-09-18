n=int(input())
a,b=0,1
c=a+b
while c<n:
    c=a+b
    if c==n:
        print("True")
        break
    else:
        a=b
        b=c
else:
    print("False")