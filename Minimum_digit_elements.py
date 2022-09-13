def fun(x):
    s=0
    while x:
        r=x%10
        s+=1
        x=x//10
    return s
n=int(input())
l=list(map(int,input().split()))
c=min(l)
v=fun(c)
sm=0
for i in l:
    r=fun(i)
    if r==v:
        sm+=1
print(sm)
        