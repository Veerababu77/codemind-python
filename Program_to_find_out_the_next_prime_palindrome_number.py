import math as m
n=int(input())
def pr(x):
    if x<2:
        return False
    for i in range(2,int(m.sqrt(x))+1):
        if x%i==0:
            return False
    return True
def pal(x):
    if str(x)==str(x)[::-1]:
        return True
    return False
while True:
    if pr(n+1) and pal(n+1):
        print(n+1)
        break
    n=n+1