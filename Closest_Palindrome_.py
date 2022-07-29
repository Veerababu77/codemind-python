n=int(input())
for i in range(n-1,1,-1):
    t=i
    te=i
    r=0
    while t>0:
        d=t%10
        r=r*10+d
        t=t//10
    if(r==te):
        l1=r
        break
for j in range(n+1,n+1000,1):
    t=j
    te=j
    r=0
    while t>0:
        d=t%10
        r=r*10+d
        t=t//10
    if r==te:
        l2=r
        break
d1=n-l1
d2=l2-n
if d1==d2 or d2==d1:
    print(l1,l2)
elif d1<d2:
    print(l1)
else:
    print(l2)