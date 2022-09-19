def fun(x):
    s=0
    while x:
        r=x%10
        s+=r
        x=x//10
    return s
n=int(input())
for i in range(n):
    if fun(n)<=9:
        print(fun(n))
        break
    else:
        n=fun(n)
else:
    print(-1)