n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=list(map(int,input().split()))
    l1.append(l)
e=0
d=0
for j in range(len(l1)):
    for k in range(m):
        if l1[j][k]%2==0:
            e+=l1[j][k]
        else:
            d+=l1[j][k]
print(e,d,end=" ")