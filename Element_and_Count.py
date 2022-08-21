n=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
le=[]
for k in lis:
    le.append(k)
    a=l.count(k)
    le.append(a)
print(*le)
    
        
    