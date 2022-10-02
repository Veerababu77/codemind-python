n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
m=[]
for j in range(len(l)):
    c=0
    for k in range(len(l1)):
        c+=l1[k][j]
    m.append(c)
print(*m)
        