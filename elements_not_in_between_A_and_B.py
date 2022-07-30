n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
if a>b:
    a,b=b,a
l1=[]
s=0
for i in range(len(l)):
    if a>l[i] or b<l[i]:
        l1.append(l[i])
if len(l1)==0:
    print(-1)
else:
    print(*l1)
        