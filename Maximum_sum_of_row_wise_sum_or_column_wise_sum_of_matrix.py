n,m=map(int,input().split())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
r=0
c=0
r=[]
for i in l:
    r.append(sum(i))
for j in range(len(l)):
    c=0
    for i in range(len(l)):
        c+=l[i][j]
    r.append(c)
print(max(r))