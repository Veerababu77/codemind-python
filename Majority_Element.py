n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in range(len(l)):
    x=l.count(l[i])
    if c<x:
        c=x
        s=l[i]
print(s)