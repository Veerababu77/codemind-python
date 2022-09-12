def fun(x):
    s=str(x)
    v=s[::-1]
    if s==v:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if fun(i):
        c+=1
print(c)
    
    