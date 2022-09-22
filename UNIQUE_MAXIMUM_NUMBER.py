n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l.count(l[i])==1:
        if c<l[i]:
            c=l[i]
if c==0:
    print(-1)
else:
    print(c)