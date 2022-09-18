n=int(input())
for i in range(n):
    x=int(input())
    v=x
    y=0
    while x:
        r=x%10
        y=y*10+r
        x=x//10
    if v==y:
        print("True")
    else:
        print("False")