from math import sqrt
def fun(x):
    if x<2:
        return 0
    for i in range(2,x):
        if x%i==0:
            return 0
    return x
n=int(input())
l=[]
t1=0
t2=0
for i in range(2,n+1):
    if fun(i)!=0:
        l.append(fun(i))
for j in l:
    for k in range(len(l)):
        if j*l[k]==n and j!=l[k]:
            t1=j
            t2=l[k]
            break
if t1!=0 and t2!=0:
    print(t2,t1,end=" ")
else:
    print(-1)