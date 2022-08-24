def fun(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if fun(i):
        c+=1
print(c)