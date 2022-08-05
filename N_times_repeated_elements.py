n=int(input())
l=list(map(int,input().split()))
m=int(input())
lis=[]
c=0
for i in l:
    if l.count(i)==m and i not in lis:
        lis.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*lis)