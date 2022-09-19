def fun(x):
    s=0
    t=x
    while x:
        r=x%10
        s=s*10+r
        x=x//10
    if t==s:
        return True
    else:
        return False
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    if fun(i):
        l.append(i)
print(*l)
        