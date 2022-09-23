n,m=map(int,input().split())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)

for j in range(n):
    c=[]
    for k in range(n):
        c.append(l[k][j])
    print(max(c))
    