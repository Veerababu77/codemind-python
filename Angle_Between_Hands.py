H,M=map(int,input().split(":"))
a=30*H-11/2*M
if a<0:
    a=a*-1
t=a
k=abs(t-360)
if t<k:
    print(t)
else:
    print(k)
