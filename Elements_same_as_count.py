n=int(input())
l=list(map(int,input().split()))
#print(l)
c=0
lis=[]
for i in l:
    if l.count(i)==i and i not in lis:
        lis.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*lis)