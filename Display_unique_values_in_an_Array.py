n=int(input())
l=list(map(int,input().split()))
c=0
r=[]
for i in l:
    if l.count(i)==1:
        r.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*r)