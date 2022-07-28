n=int(input())
a,b=0,1
l=[0,1]
l1=[]
l2=[]
for i in range(n):
    c=a+b
    l.append(c)
    a=b
    b=c
if n in l:
    l.remove(n)
for j in range(len(l)):
    if l[j]<n:
        l1.append(l[j])
    else:
        l2.append(l[j])
ln=len(l1)
r1=l1[ln-1]
r2=l2[0]
d1=n-r1
d2=r2-n
if d1==d2:
    print(r1,r2)
elif d1<d2:
    print(r1)
else:
    print(r2)

        
