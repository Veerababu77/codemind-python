import math as m
def fun(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if fun(i):
        l1.append(i)
s=sum(l1)/len(l1)
print("%0.2f"%s)
