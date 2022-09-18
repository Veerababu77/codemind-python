def fun(x):
    v=x
    while x!=0:
        r=x%10
        x=x//10
        if r==0 or v%r!=0:
            return False
    else:
        return True
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    if i<10:
        l.append(i)
    elif fun(i):
        l.append(i)
print(*l)
