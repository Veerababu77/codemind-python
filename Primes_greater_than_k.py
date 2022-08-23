def fun(v):
    s=0
    for i in range(1,v+1):
        if v%i==0:
            s+=1
    if s==2:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
x=int(input())
c=0
for j in l:
    if j>=x and fun(j):
        c+=1
print(c)