n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
e=0
d=0
for j in range(len(l1)):
    if j%2==1:
        for k in range(m):
            d+=l1[j][k]
    else:
        for w in range(m):
            e+=l1[j][w]
print(e,d,end=" ")