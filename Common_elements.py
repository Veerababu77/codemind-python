n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
l3=[]
for i in l1:
    if i in l2:
        l.append(i)
for i in l:
    if i not in l3:
        l3.append(i)
print(*l3)
